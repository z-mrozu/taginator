from . import importer, viewer, extractor

class Taginator():
    def __init__(self):
        self.importers = []
        self.viewer = viewer.Viewer()
        self.notes = {}
        self.extractors = [extractor.DateExtractor()]

    def list_notes(self):
        self.viewer.view_listed(self.notes)

    def import_notes(self, path):
        imp = importer.TxtImporter(path)
        imp.import_notes()
        processed = self.__process_notes(imp.get_notes())
        self.notes.update(processed)
        self.importers.append(imp)

    def __process_notes(self, dict):
        for extractor in self.extractors:
            for name, note in dict.items():
                note.set_extracted_values(extractor.get_name(), extractor.extract(note))
        return dict
