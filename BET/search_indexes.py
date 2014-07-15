__author__ = 'yaxxu'
from haystack import indexes
from BET.models import Schematic,Combine


# class SchematicIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     part_number = indexes.CharField(model_attr='part_number')
#     pins = indexes.IntegerField(model_attr='pins')
#
#     def get_model(self):
#         return Schematic

class CombineIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    part_number = indexes.CharField(model_attr='part_number')
    pins = indexes.IntegerField(model_attr='pins')

    def get_model(self):
        return Combine
