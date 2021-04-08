import datetime as dt
import logging
import json
import os

from PyQt5.QtCore import QThread, pyqtSignal

class RelationshipExtractor(QThread):
    signal1 = pyqtSignal()
    signal2 = pyqtSignal()
    signal3 = pyqtSignal()

    def __init__(self, files, delta_time):
        QThread.__init__(self)
        self.files = files
        self.delta_time = delta_time

    def run(self):
        logging.debug("extract_relationships(): Instantiated")
        delta_time = [int(value) for value in self.delta_time]
        artifact_list = self.retrieve_json_data(self.files)
        artifact_list = self.restructure_artifacts(artifact_list)
        relationship_list, relationship_tracker = self.find_relationships(artifact_list, delta_time)
        relationship_list = self.clean_relationship_list(artifact_list, relationship_tracker)
        self.create_relationship_file(relationship_list)
        logging.debug("extract_relationships(): Complete")
    
    def retrieve_json_data(self, files):
        logging.debug("retrieve_json_data(): Instantiated")
        temp_list = []
        for file in files:
            json_file = open(file)
            temp_list.append(json.load(json_file))
            json_file.close()
        logging.debug("retrieve_json_data(): Complete")
        self.signal3.emit()
        return temp_list

    def restructure_artifacts(self, artifact_list):
        logging.debug("restructure_artifacts(): Instantiated")
        index1 = 0
        index2 = 0
        artifact_counter = 0
        updated_artifact_list = []
        while index1 < len(artifact_list):
            while index2 < len(artifact_list[index1]):
                temp_key = list(artifact_list[index1][index2].keys())[0]
                artifact_list[index1][index2]['Artifact_id'] = artifact_counter
                if temp_key == 'traffic_xy_id':
                    del artifact_list[index1][index2]['className']
                elif temp_key == 'traffic_all_id':
                    del artifact_list[index1][index2]['className']
                elif temp_key == 'timed_id':
                    del artifact_list[index1][index2]['classname']
                    del artifact_list[index1][index2]['type']
                elif temp_key == 'keypresses_id':
                    del artifact_list[index1][index2]['className']
                elif temp_key == 'clicks_id':
                    del artifact_list[index1][index2]['classname']
                    del artifact_list[index1][index2]['type']
                elif temp_key == 'auditd_id':
                    del artifact_list[index1][index2]['className']
                else:
                    print('A new dissector has been identified (' + temp_key + '), and requires implementation.')
                del artifact_list[index1][index2][temp_key]
                artifact_list[index1][index2]['start'] = artifact_list[index1][index2]['start'].replace('T', ' ')
                try:
                    artifact_list[index1][index2]['start'] = dt.datetime.strptime(artifact_list[index1][index2]['start'], '%Y-%m-%d %H:%M:%S.%f') # If time contains milliseconds
                except:
                    artifact_list[index1][index2]['start'] = dt.datetime.strptime(artifact_list[index1][index2]['start'], '%Y-%m-%d %H:%M:%S')  # If time only has up to seconds
                artifact_list[index1][index2]['Artifact_Relationships'] = []
                updated_artifact_list.append(artifact_list[index1][index2])
                self.signal1.emit()
                artifact_counter += 1
                index2 += 1
            index2 = 0
            index1 += 1
        logging.debug("restructure_artifacts(): Complete")
        self.signal3.emit()
        return updated_artifact_list

    def find_relationships(self, artifact_list, delta_time):
        logging.debug("find_relationships(): Instantiated")
        relationship_tracker = []
        time_dif = dt.timedelta(seconds=delta_time[0])
        time_dif = time_dif + dt.timedelta(milliseconds=delta_time[1])
        index1 = 0
        index2 = 0
        while index1 < (len(artifact_list) - 1):
            date_dif = artifact_list[index1]['start'] + time_dif
            index2 = index1 + 1
            while index2 < len(artifact_list):
                if date_dif >= artifact_list[index2]['start']:
                    if artifact_list[index1]['Artifact_id'] not in relationship_tracker:
                        relationship_tracker.append(artifact_list[index1]['Artifact_id'])
                    if artifact_list[index2]['Artifact_id'] not in relationship_tracker:
                        relationship_tracker.append(artifact_list[index2]['Artifact_id'])
                    artifact_list[index1]['Artifact_Relationships'].append(artifact_list[index2]['Artifact_id'])
                    self.signal2.emit()
                index2 += 1
            index1 += 1
        logging.debug("find_relationships(): Complete")
        self.signal3.emit()
        return artifact_list, relationship_tracker

    def clean_relationship_list(self, artifact_list, relationship_tracker):
        logging.debug("clean_relationship_list(): Instantiated")
        index = 0
        updated_artifact_list = artifact_list
        while index < len(artifact_list):
            if artifact_list[index]['Artifact_id'] not in relationship_tracker:
                del updated_artifact_list[index]
            try:
                updated_artifact_list[index]['start'] = updated_artifact_list[index]['start'].strftime('%Y-%m-%d %H:%M:%S.%f') # If time contains milliseconds
            except:
                updated_artifact_list[index]['start'] = updated_artifact_list[index]['start'].strftime('%Y-%m-%d %H:%M:%S') # If time only has up to seconds
            index += 1
        logging.debug("clean_relationship_list(): Complete")
        self.signal3.emit()
        return updated_artifact_list

    def create_relationship_file(self, relationship_list):
        logging.debug("create_relationship_file(): Instantiated")
        with open(os.getcwd() + '/../GeneratedData/Relationships.JSON', 'w') as outfile:
            json.dump(relationship_list, outfile, ensure_ascii=False, indent=4)
        self.signal3.emit()
        logging.debug("create_relationship_file(): Complete")