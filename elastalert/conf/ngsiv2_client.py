import copy
from bravado.client import SwaggerClient
import click

fiware_nsgiv2_openapi_spec = {
    "swagger": "2.0",
    "info": {
        "version": "v2",
        "title": "NGSIV2 management API",
        "description": "The FIWARE NGSI (Next Generation Service Interface) API"
    },
    "host": "localhost:1025",
    "basePath": "/v2",
    "schemes": [
        "http"
    ],
    "securityDefinitions": {
        "OauthSecurity": {
            "type": "apiKey",
            "name": "X-AUTH-token",
            "in": "header"
        }
    },
    "security": [
        {
            #"OauthSecurity": []
        }
    ],
    "paths": {
        "/entities": {
            "get": {
                "description": "Gets entities objects.",
                "tags": [
                    "Entity"
                ],
                "summary": "Entity list",
                "operationId": "get_entities",
                "consumes": [],
                "produces": [
                    "application/json",
                    "text/json"
                ],
                "parameters": [
                    {
                        "$ref": "#/parameters/id_filter"
                    }
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "title": "ArrayOfEntities",
                            "type": "array",
                            "items": {
                                "$ref": "#/definitions/Entity"
                            }
                        }
                    },
                    "401": {
                        "description": "Unauthorized",
                        "schema": {
                            "type": "string"
                        }
                    },
                    "default": {
                        "description": "Bad Request. See response body for details",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "post": {
                "tags": [
                    "Entity"
                ],
                "summary": "Creates an entity",
                "description": "Add an entity",
                "operationId": "create_entity",
                "consumes": [
                    "application/json",
                    "text/json",
                    "application/x-www-form-urlencoded"
                ],
                "produces": [],
                "parameters": [
                    {
                        "name": "entity",
                        "in": "body",
                        "description": "Entity to create",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/Entity"
                        }
                    }
                ],
                "responses": {
                    "201": {
                        "description": "The entity has been created"
                    },
                    "default": {
                        "description": "Bad Request. See response body for details",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/entities/{entity_id}": {
            "parameters": [
                    {
                        "name": "entity_id",
                        "in": "path",
                        "description": "The entity id",
                        "required": True,
                        "type": "string"
                    }
                ],
            "get": {
                "description": "Gets an 'entity' object.",
                "tags": [
                    "Entity"
                ],
                "summary": "Entity",
                "operationId": "get_entity",
                "consumes": [],
                "produces": [
                    "application/json",
                    "text/json"
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/Entity"
                        }
                    },
                    "default": {
                        "description": "Bad Request. See response body for details",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "delete": {
                "description": "Delete an 'entity' object.",
                "tags": [
                    "Entity"
                ],
                "summary": "Delete an Entity",
                "operationId": "delete_entity",
                "consumes": [],
                "produces": [],
                "responses": {
                    "204": {
                        "description": "OK"
                    },
                    "default": {
                        "description": "Bad Request. See response body for details",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        },
        "/entities/{entity_id}/attrs": {
            "get": {
                "description": "Gets attributes of an 'entity'",
                "tags": [
                    "Entity"
                ],
                "parameters": [
                    {
                        "name": "entity_id",
                        "in": "path",
                        "description": "The entity id",
                        "required": True,
                        "type": "string"
                    }
                ],
                "summary": "Entity",
                "operationId": "get_entity_attrs",
                "consumes": [],
                "produces": [
                    "application/json",
                    "text/json"
                ],
                "responses": {
                    "200": {
                        "description": "OK",
                        "schema": {
                            "$ref": "#/definitions/AttributeList"
                        }
                    },
                    "default": {
                        "description": "Bad Request. See response body for details",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            },
            "put": {
                "description": "Update attributes of an 'entity'",
                "tags": [
                    "Entity"
                ],
                "summary": "Entity",
                "operationId": "set_entity_attrs",
                "consumes": [
                    "application/json",
                    "text/json",
                    "application/x-www-form-urlencoded"
                ],
                "produces": [
                    "application/json",
                    "text/json"
                ],
                "parameters": [
                    {
                        "name": "entity_id",
                        "in": "path",
                        "description": "The entity id",
                        "required": True,
                        "type": "string"
                    },
                    {
                        "name": "attribute_list",
                        "in": "body",
                        "description": "Attributes to update",
                        "required": True,
                        "schema": {
                            "$ref": "#/definitions/AttributeList"
                        }
                    }
                ],
                "responses": {
                    "204": {
                        "description": "Entity Attr List updated OK"
                    },
                    "default": {
                        "description": "Bad Request. See response body for details",
                        "schema": {
                            "$ref": "#/definitions/Error"
                        }
                    }
                }
            }
        }
    },
    "parameters": {
        "id_filter": {
            "name": "id_pp",
            "description": "Query filter by id",
            "in": "query",
            "type": "string"
        }
    },
    "definitions": {
        "Entity": {
            "description": "Entity information",
            "type": "object",
            "allOf": [
                {
                    "$ref": "#/definitions/EntityAttrs"
                },
                {
                    "$ref": "#/definitions/AttributeList"
                }
            ]
        },
        "EntityAttrs": {
            "description": "Entity information",
            "type": "object",
            "required": [
                "id"
            ],
            "properties": {
                "id": {
                    "description": "Public unique identifier of the entity",
                    "type": "string"
                },
                "type": {
                    "description": "The friendly name of the account for display purposes",
                    "type": "string"
                }
            }
        },
        "AttributeList": {
            "description": "Entity Attributes",
            "type": "object",
            "properties": {
                "temperature": {
                    "$ref": "#/definitions/Attribute"
                },
                "pressure": {
                    "$ref": "#/definitions/Attribute"
                }
            }
        },
        "Attribute": {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string"
                },
                "value": {
                    "type": "string"
                }
            }
        },
        "Error": {
            "required": [
                "error"
            ],
            "type": "object",
            "properties": {
                "error": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                }
            }
        }
    }
}

SOURCE_IP_1 = '1.1.1.1'
SOURCE_IP_2 = '2.2.2.2'

oauth_token = 'f5Q4jL5RlqNAXdZS4ztQ93sUpPSOhn'

CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}

@click.group(help='Script to manage \'NGSIV2 API\'', context_settings=CONTEXT_SETTINGS)
def ngsiv2_setup():
    pass


@ngsiv2_setup.group(help='Manage Entities using NGSIV2 API')
def entity():
    pass


@entity.command('create', help='Create an NGSIV2 Entity')
@click.option('-id', '--uuid', required=True, type=str, help='ID of device. ')
@click.option('-t', '--temperature', required=True, type=str, help='Temperature attr')
@click.option('-p', '--pressure', required=True, type=str, help='Pressure attr. ')
@click.option('-ip', '--source_ip', required=True, type=str, help='Source IP. ')
def create_entity(uuid, temperature, pressure, source_ip):
    """
    Manage create operations
    """
    client = NGSIv2Client()

    client.set_source_ip(source_ip)

    client.create_entity(id=uuid, temperature=temperature, pressure=pressure)


@entity.command('update', help='Update an NGSIV2 Entity')
@click.option('-id', '--uuid', required=True, type=str, help='ID of device. ')
@click.option('-t', '--temperature', required=True, type=str, help='Temperature attr')
@click.option('-p', '--pressure', required=True, type=str, help='Pressure attr. ')
@click.option('-ip', '--source_ip', required=True, type=str, help='Source IP. ')
def update_entity(uuid, temperature, pressure, source_ip):
    """
    Manage update operations
    """
    client = NGSIv2Client()

    client.set_source_ip(source_ip)

    client.set_entity_attrs(entity_id=uuid, temperature=temperature, pressure=pressure)


@entity.command('get', help='Get NGSIV2 Entity')
@click.option('-id', '--uuid', required=True, type=str, help='ID of device. ')
def get_entity(uuid):
    """
    Manage get operation
    """
    client = NGSIv2Client()

    print(client.get_entity(entity_id=uuid))


@entity.command('get_all', help='Get all NGSIV2 Entities')
def get_entity():
    """
    Manage get operation
    """
    client = NGSIv2Client()

    print(client.get_entities())


class NGSIv2Client:
    def __init__(self):
        self.client = SwaggerClient.from_spec(fiware_nsgiv2_openapi_spec)
        self.options = {'headers': {}}

        self.id=''
        self.type=''
        self.temperature=''
        self.pressure=''

    def set_oauth_token(self, oauth_token):
        """
        """
        self.options.get("headers").update({'X-AUTH-token': oauth_token})

    def set_source_ip(self, ip):
        """
        """
        self.options.get("headers").update({'X-Real-IP': ip})

    def get_attribute_model(self, type, value):
        """
        """
        Attribute = self.client.get_model('Attribute')
        return Attribute(type=type,
                         value=value)

    def get_entity_attrs_model(self, temperature, pressure):
        """
        """
        temperature_attr = self.get_attribute_model(type="int", value=temperature)
        pressure_attr = self.get_attribute_model(type="int", value=pressure)

        AttributeList = self.client.get_model('AttributeList')
        return AttributeList(temperature=temperature_attr,
                             pressure=pressure_attr)

    def get_entity_model(self, id, type, temperature, pressure):
        """
        """
        Entity = self.client.get_model('Entity')
        return Entity(id=id,
                      type=type,
                      temperature=self.get_attribute_model(type="int", value=temperature),
                      pressure=self.get_attribute_model(type="int", value=pressure))

    def create_entity(self, id, temperature, pressure):
        """
        Create entity
        """
        entity = self.get_entity_model(id=id, type="sensor", temperature=temperature, pressure=pressure)

        return self.client.Entity.create_entity(entity=entity,
                                                _request_options=copy.deepcopy(self.options)).result()
    def get_entities(self):
        """
        Get entities
        """
        return self.client.Entity.get_entities(_request_options=copy.deepcopy(self.options)).result()

    def get_entity(self, entity_id):
        """
        Get entity
        """
        return self.client.Entity.get_entity(entity_id=entity_id,
                                             _request_options=copy.deepcopy(self.options)).result()

    def get_entity_attrs(self, entity_id):
        """
        Get entity
        """
        return self.client.Entity.get_entity_attrs(entity_id=entity_id,
                                              _request_options=copy.deepcopy(self.options)).result()

    def set_entity_attrs(self, entity_id, temperature, pressure):
        """
        Set entity
        """
        new_attr_list = self.get_entity_attrs_model(temperature=temperature, pressure=pressure)

        return self.client.Entity.set_entity_attrs(entity_id=entity_id,
                                              attribute_list=new_attr_list,
                                              _request_options=copy.deepcopy(self.options)).result()

    def delete_entity(self, entity_id):
        """
        Get entity
        """
        return self.client.Entity.delete_entity(entity_id=entity_id,
                                                _request_options=copy.deepcopy(self.options)).result()

if __name__ == '__main__':

    ngsiv2_setup()

