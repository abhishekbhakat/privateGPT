from langchain.document_loaders import UnstructuredMarkdownLoader
markdown_path = r"source_documents\\Pyspy.md"
loader = UnstructuredMarkdownLoader(markdown_path)
data = loader.load()