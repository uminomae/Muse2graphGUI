import pickle
import os

CONFIG_FILE = 'config/app_config.pkl'

def save_config(graph_title, data_span, selection_type):
    configure = {
        'graph_title': graph_title,
        'data_span': data_span,
        'selection_type': selection_type
    }
    with open(CONFIG_FILE, 'wb') as f:
        pickle.dump(configure, f)

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'rb') as f:
            return pickle.load(f)
    return {'graph_title': None, 'data_span': None, 'selection_type': 'recent'}
