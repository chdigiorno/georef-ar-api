from elasticsearch_params import LOWCASE_ASCII_NORMALIZER
from elasticsearch_params import NAME_ANALYZER
from elasticsearch_params import NAME_ANALYZER_SYNONYMS

# Mapeos de entidades para Elasticsearch
# Por cada entidad, se define un mapeo sin geometría, con campos indexados,
# y otro con geometría, con el resto de los campos sin indexar.
# La separación en dos mapeos por entidad se debe a que las geometrías tienden
# a aumentar significativamente el tamaño de los documentos, por lo que la
# performance de la búsqueda por id/texto/etc se ve disminuida.

# https://www.elastic.co/guide/en/elasticsearch/reference/current/general-recommendations.html#maximum-document-size

TIMESTAMP = {
    'type': 'date',
    'format': 'epoch_second',
    'index': False
}

MAP_STATE = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword'},
            'timestamp': TIMESTAMP,
            'nombre': {
                'type': 'text',
                'analyzer': NAME_ANALYZER_SYNONYMS,
                'search_analyzer': NAME_ANALYZER,
                'fields': {
                    'exacto': {
                        'type': 'keyword',
                        'normalizer': LOWCASE_ASCII_NORMALIZER
                    }
                }
            },
            'lat': {'type': 'keyword'},
            'lon': {'type': 'keyword'}
        }
    }
}

MAP_STATE_GEOM = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword', 'index': False},
            'timestamp': TIMESTAMP,
            'nombre': {'type': 'keyword', 'index': False},
            'lat': {'type': 'keyword', 'index': False},
            'lon': {'type': 'keyword', 'index': False},
            'geometria': {'type': 'geo_shape'}
        }
    }
}

MAP_DEPT = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword'},
            'timestamp': TIMESTAMP,
            'nombre': {
                'type': 'text',
                'analyzer': NAME_ANALYZER_SYNONYMS,
                'search_analyzer': NAME_ANALYZER,
                'fields': {
                    'exacto': {
                        'type': 'keyword',
                        'normalizer': LOWCASE_ASCII_NORMALIZER
                    }
                }
            },
            'lat': {'type': 'keyword'},
            'lon': {'type': 'keyword'},
            'provincia': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    }
                }
            }
        }
    }
}

MAP_DEPT_GEOM = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword', 'index': False},
            'timestamp': TIMESTAMP,
            'nombre': {'type': 'keyword', 'index': False},
            'lat': {'type': 'keyword', 'index': False},
            'lon': {'type': 'keyword', 'index': False},
            'provincia': {'type': 'object', 'enabled': False},
            'geometria': {'type': 'geo_shape'}
        }
    }
}

MAP_MUNI = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword'},
            'timestamp': TIMESTAMP,
            'nombre': {
                'type': 'text',
                'analyzer': NAME_ANALYZER_SYNONYMS,
                'search_analyzer': NAME_ANALYZER,
                'fields': {
                    'exacto': {
                        'type': 'keyword',
                        'normalizer': LOWCASE_ASCII_NORMALIZER
                    }
                }
            },
            'lat': {'type': 'keyword'},
            'lon': {'type': 'keyword'},
            'departamento': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    }
                }
            },
            'provincia': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    }
                }
            }
        }
    }
}

MAP_MUNI_GEOM = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword', 'index': False},
            'timestamp': TIMESTAMP,
            'nombre': {'type': 'keyword', 'index': False},
            'lat': {'type': 'keyword', 'index': False},
            'lon': {'type': 'keyword', 'index': False},
            'departamento': {'type': 'object', 'enabled': False},
            'provincia': {'type': 'object', 'enabled': False},
            'geometria': {'type': 'geo_shape'}
        }
    }
}

MAP_SETTLEMENT = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword'},
            'timestamp': TIMESTAMP,
            'nombre': {
                'type': 'text',
                'analyzer': NAME_ANALYZER_SYNONYMS,
                'search_analyzer': NAME_ANALYZER,
                'fields': {
                    'exacto': {
                        'type': 'keyword',
                        'normalizer': LOWCASE_ASCII_NORMALIZER
                    }
                }
            },
            'tipo': {'type': 'keyword'},
            'lat': {'type': 'keyword'},
            'lon': {'type': 'keyword'},
            'municipio': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    },
                }
            },
            'departamento': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    }
                }
            },
            'provincia': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    }
                }
            }
        }
    }
}

MAP_SETTLEMENT_GEOM = {
    '_doc': {
        'properties': {
            'id': {'type': 'keyword', 'index': False},
            'timestamp': TIMESTAMP,
            'nombre': {'type': 'keyword', 'index': False},
            'tipo': {'type': 'keyword', 'index': False},
            'lat': {'type': 'keyword', 'index': False},
            'lon': {'type': 'keyword', 'index': False},
            'municipio': {'type': 'object', 'enabled': False},
            'departamento': {'type': 'object', 'enabled': False},
            'provincia': {'type': 'object', 'enabled': False},
            'geometria': {'type': 'geo_shape'}
        }
    }
}

MAP_STREET = {
    '_doc': {
        'properties': {
            'nomenclatura': {
                'type': 'text',
                'index': False
            },
            'id': {'type': 'keyword'},
            'timestamp': TIMESTAMP,
            'nombre': {
                'type': 'text',
                'analyzer': NAME_ANALYZER_SYNONYMS,
                'search_analyzer': NAME_ANALYZER,
                'fields': {
                    'exacto': {
                        'type': 'keyword',
                        'normalizer': LOWCASE_ASCII_NORMALIZER
                    }
                }
            },
            'tipo': {
                'type': 'text',
                'analyzer': NAME_ANALYZER_SYNONYMS,
                'search_analyzer': NAME_ANALYZER
            },
            'inicio_derecha': {
                'type': 'integer'
            },
            'inicio_izquierda': {
                'type': 'integer',
                # Solo START_R y END_L son necesarias para la busqueda de
                # calles por altura.
                'index': False
            },
            'fin_derecha': {
                'type': 'integer',
                # Solo START_R y END_L son necesarias para la busqueda de
                # calles por altura.
                'index': False
            },
            'fin_izquierda': {
                'type': 'integer'
            },
            'geometria': {
                'type': 'text',
                'index': False
            },
            'departamento': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    }
                }
            },
            'provincia': {
                'type': 'object',
                'dynamic': 'strict',
                'properties': {
                    'id': {'type': 'keyword'},
                    'nombre': {
                        'type': 'text',
                        'analyzer': NAME_ANALYZER_SYNONYMS,
                        'search_analyzer': NAME_ANALYZER,
                        'fields': {
                            'exacto': {
                                'type': 'keyword',
                                'normalizer': LOWCASE_ASCII_NORMALIZER
                            }
                        }
                    }
                }
            }
        }
    }
}
