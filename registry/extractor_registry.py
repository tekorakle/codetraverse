from extractors.haskell_extractor import HaskellComponentExtractor
from extractors.python_extractor import PythonComponentExtractor
from extractors.rescript_extractor import RescriptComponentExtractor
from extractors.rust_extractor import RustComponentExtractor
from extractors.go_extractor import GoComponentExtractor
from extractors.typescript_extractor import TypeScriptComponentExtractor

def get_extractor(language: str):
    lang = language.lower()
    if lang == "haskell":
        return HaskellComponentExtractor()
    if lang == "python":
        return PythonComponentExtractor()
    if lang == "rescript":
        return RescriptComponentExtractor()
    if lang == "rust":
        return RustComponentExtractor()
    if lang == "golang":
        return GoComponentExtractor()
    if lang == "typescript":
        return TypeScriptComponentExtractor()
    raise ValueError(f"No extractor for language: {language}")
