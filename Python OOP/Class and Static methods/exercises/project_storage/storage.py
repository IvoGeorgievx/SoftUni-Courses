from class_and_static_methods.exercise.project_storaaaage.category import Category
from class_and_static_methods.exercise.project_storaaaage.document import Document
from class_and_static_methods.exercise.project_storaaaage.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category in self.categories:
            return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic in self.topics:
            return
        self.topics.append(topic)

    def add_document(self, document: Document):
        if document in self.documents:
            return
        self.documents.append(document)

    def __find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity

    def edit_category(self, category_id, new_name):
        current_category = self.__find_by_id(self.categories, category_id)
        current_category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        current_topic = self.__find_by_id(self.topics, topic_id)
        current_topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        current_doc = self.__find_by_id(self.documents, document_id)
        current_doc.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__find_by_id(self.categories, category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__find_by_id(self.topics, topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        doc = self.__find_by_id(self.documents, document_id)
        self.documents.remove(doc)

    def get_document(self, document_id):
        return self.__find_by_id(self.documents, document_id)

    def __repr__(self):
        return f'\n'.join([repr(x) for x in self.documents])
