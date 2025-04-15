import ast
from pathlib import Path

# NOTE: <= 3.8
import astor


class ObfuscatorDocstring(ast.NodeTransformer):
    @staticmethod
    def run_inplace(path: Path):
        with path.open("rt", encoding="utf-8") as fp:
            code = fp.read()

        tree = ast.parse(code)
        tree = ObfuscatorDocstring().visit(tree)
        ast.fix_missing_locations(tree)

        obfuscated_code = astor.to_source(tree)

        with path.open("wt", encoding="utf-8") as fp:
            fp.write(obfuscated_code)

    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            if isinstance(node.body[0].value.value, str):
                node.body.pop(0)
        return node

    def visit_AsyncFunctionDef(self, node):
        return self.visit_FunctionDef(node)

    def visit_ClassDef(self, node):
        self.generic_visit(node)
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            if isinstance(node.body[0].value.value, str):
                node.body.pop(0)
        return node

    def visit_Module(self, node):
        self.generic_visit(node)
        if node.body and isinstance(node.body[0], ast.Expr) and isinstance(node.body[0].value, ast.Constant):
            if isinstance(node.body[0].value.value, str):
                node.body.pop(0)
        return node

