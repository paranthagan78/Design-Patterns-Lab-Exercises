from abc import ABC, abstractmethod

# State interface
class State(ABC):
    @abstractmethod
    def publish_document(self):
        pass

# Concrete states
class DraftState(State):
    def publish_document(self):
        print("Document is in the Draft state. Publishing...")
        # Logic to publish the document
        print("Document published successfully.")
        return PublishedState()

class PublishedState(State):
    def publish_document(self):
        print("Document is already published. No further action needed.")
        return self

# Context class
class DocumentEditor:
    def __init__(self):
        self.state = DraftState()

    def get_state(self):
        return type(self.state).__name__

    def publish_document(self):
        self.state = self.state.publish_document()

# Example usage
document_editor = DocumentEditor()

# Publish document in the Draft state
document_editor.publish_document()
print("Current state:", document_editor.get_state())

# Try to publish document again
document_editor.publish_document()
print("Current state:", document_editor.get_state())
