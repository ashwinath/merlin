# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.7.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PredictionJobConfig(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'version': 'str',
        'kind': 'str',
        'name': 'str',
        'bigquery_source': 'PredictionJobConfigBigquerySource',
        'gcs_source': 'PredictionJobConfigGcsSource',
        'model': 'PredictionJobConfigModel',
        'bigquery_sink': 'PredictionJobConfigBigquerySink',
        'gcs_sink': 'PredictionJobConfigGcsSink'
    }

    attribute_map = {
        'version': 'version',
        'kind': 'kind',
        'name': 'name',
        'bigquery_source': 'bigquery_source',
        'gcs_source': 'gcs_source',
        'model': 'model',
        'bigquery_sink': 'bigquery_sink',
        'gcs_sink': 'gcs_sink'
    }

    def __init__(self, version=None, kind=None, name=None, bigquery_source=None, gcs_source=None, model=None, bigquery_sink=None, gcs_sink=None):  # noqa: E501
        """PredictionJobConfig - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._kind = None
        self._name = None
        self._bigquery_source = None
        self._gcs_source = None
        self._model = None
        self._bigquery_sink = None
        self._gcs_sink = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if kind is not None:
            self.kind = kind
        if name is not None:
            self.name = name
        if bigquery_source is not None:
            self.bigquery_source = bigquery_source
        if gcs_source is not None:
            self.gcs_source = gcs_source
        if model is not None:
            self.model = model
        if bigquery_sink is not None:
            self.bigquery_sink = bigquery_sink
        if gcs_sink is not None:
            self.gcs_sink = gcs_sink

    @property
    def version(self):
        """Gets the version of this PredictionJobConfig.  # noqa: E501


        :return: The version of this PredictionJobConfig.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PredictionJobConfig.


        :param version: The version of this PredictionJobConfig.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def kind(self):
        """Gets the kind of this PredictionJobConfig.  # noqa: E501


        :return: The kind of this PredictionJobConfig.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this PredictionJobConfig.


        :param kind: The kind of this PredictionJobConfig.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this PredictionJobConfig.  # noqa: E501


        :return: The name of this PredictionJobConfig.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PredictionJobConfig.


        :param name: The name of this PredictionJobConfig.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def bigquery_source(self):
        """Gets the bigquery_source of this PredictionJobConfig.  # noqa: E501


        :return: The bigquery_source of this PredictionJobConfig.  # noqa: E501
        :rtype: PredictionJobConfigBigquerySource
        """
        return self._bigquery_source

    @bigquery_source.setter
    def bigquery_source(self, bigquery_source):
        """Sets the bigquery_source of this PredictionJobConfig.


        :param bigquery_source: The bigquery_source of this PredictionJobConfig.  # noqa: E501
        :type: PredictionJobConfigBigquerySource
        """

        self._bigquery_source = bigquery_source

    @property
    def gcs_source(self):
        """Gets the gcs_source of this PredictionJobConfig.  # noqa: E501


        :return: The gcs_source of this PredictionJobConfig.  # noqa: E501
        :rtype: PredictionJobConfigGcsSource
        """
        return self._gcs_source

    @gcs_source.setter
    def gcs_source(self, gcs_source):
        """Sets the gcs_source of this PredictionJobConfig.


        :param gcs_source: The gcs_source of this PredictionJobConfig.  # noqa: E501
        :type: PredictionJobConfigGcsSource
        """

        self._gcs_source = gcs_source

    @property
    def model(self):
        """Gets the model of this PredictionJobConfig.  # noqa: E501


        :return: The model of this PredictionJobConfig.  # noqa: E501
        :rtype: PredictionJobConfigModel
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this PredictionJobConfig.


        :param model: The model of this PredictionJobConfig.  # noqa: E501
        :type: PredictionJobConfigModel
        """

        self._model = model

    @property
    def bigquery_sink(self):
        """Gets the bigquery_sink of this PredictionJobConfig.  # noqa: E501


        :return: The bigquery_sink of this PredictionJobConfig.  # noqa: E501
        :rtype: PredictionJobConfigBigquerySink
        """
        return self._bigquery_sink

    @bigquery_sink.setter
    def bigquery_sink(self, bigquery_sink):
        """Sets the bigquery_sink of this PredictionJobConfig.


        :param bigquery_sink: The bigquery_sink of this PredictionJobConfig.  # noqa: E501
        :type: PredictionJobConfigBigquerySink
        """

        self._bigquery_sink = bigquery_sink

    @property
    def gcs_sink(self):
        """Gets the gcs_sink of this PredictionJobConfig.  # noqa: E501


        :return: The gcs_sink of this PredictionJobConfig.  # noqa: E501
        :rtype: PredictionJobConfigGcsSink
        """
        return self._gcs_sink

    @gcs_sink.setter
    def gcs_sink(self, gcs_sink):
        """Sets the gcs_sink of this PredictionJobConfig.


        :param gcs_sink: The gcs_sink of this PredictionJobConfig.  # noqa: E501
        :type: PredictionJobConfigGcsSink
        """

        self._gcs_sink = gcs_sink

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PredictionJobConfig, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PredictionJobConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
