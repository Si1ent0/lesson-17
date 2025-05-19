# POST
post_users = {
    "additionalProperties": False,
    "properties": {
        "id": {
            "type": "string"
        },
        "createdAt": {
            "type": "string"
        },
        "job": {
            "type": "string"
        },
        "name": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "createdAt",
        "job",
        "name"
    ]
}

# PUT
put_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "job": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "job",
    "updatedAt"
  ]
}

# PATCH
patch_user_name_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "name": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "name",
    "updatedAt"
  ]
}

patch_user_job_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "job": {
      "type": "string"
    },
    "updatedAt": {
      "type": "string"
    }
  },
  "required": [
    "job",
    "updatedAt"
  ]
}