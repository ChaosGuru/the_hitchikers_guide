class ContextManager():
    def __init__(self, text: str):
        self.text = text

    def __enter__(self):
        print('Context Manager ENTER')
        return self.text[:-1]

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        print('Context Manager EXIT')