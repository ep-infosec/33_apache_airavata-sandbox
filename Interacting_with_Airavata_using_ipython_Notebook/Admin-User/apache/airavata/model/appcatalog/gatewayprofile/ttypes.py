#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import apache.airavata.model.appcatalog.computeresource.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class ComputeResourcePreference:
  """
  Gateway specific preferences for a Computer Resource

  computeResourceId:
    Corelate the preference to a compute resource.

  overridebyAiravata:
    If turned true, Airavata will override the preferences of better alternatives exist.

  loginUserName:
    If turned true, Airavata will override the preferences of better alternatives exist.

  preferredJobSubmissionProtocol:
    For resources with multiple job submission protocols, the gateway can pick a preferred option.

  preferredDataMovementProtocol:
    For resources with multiple data movement protocols, the gateway can pick a preferred option.

  preferredBatchQueue:
   Gateways can choose a defualt batch queue based on average job dimention, reservations or other metrics.

  scratchLocation:
   Path to the local scratch space on a HPC cluster. Typically used to create working directory for job execution.

  allocationProjectNumber:
   Typically used on HPC machines to charge computing usage to a account number. For instance, on XSEDE once an
     allocation is approved, an allocation number is assigned. Before passing this number with job submittions, the
     account to be used has to be added to the allocation.

  resourceSpecificCredentialStoreToken:
   Resource specific credential store token. If this token is specified, then it is superceeded by the gateway's
    default credential store.


  Attributes:
   - computeResourceId
   - overridebyAiravata
   - loginUserName
   - preferredJobSubmissionProtocol
   - preferredDataMovementProtocol
   - preferredBatchQueue
   - scratchLocation
   - allocationProjectNumber
   - resourceSpecificCredentialStoreToken
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'computeResourceId', None, None, ), # 1
    (2, TType.BOOL, 'overridebyAiravata', None, True, ), # 2
    (3, TType.STRING, 'loginUserName', None, None, ), # 3
    (4, TType.I32, 'preferredJobSubmissionProtocol', None, None, ), # 4
    (5, TType.I32, 'preferredDataMovementProtocol', None, None, ), # 5
    (6, TType.STRING, 'preferredBatchQueue', None, None, ), # 6
    (7, TType.STRING, 'scratchLocation', None, None, ), # 7
    (8, TType.STRING, 'allocationProjectNumber', None, None, ), # 8
    (9, TType.STRING, 'resourceSpecificCredentialStoreToken', None, None, ), # 9
  )

  def __init__(self, computeResourceId=None, overridebyAiravata=thrift_spec[2][4], loginUserName=None, preferredJobSubmissionProtocol=None, preferredDataMovementProtocol=None, preferredBatchQueue=None, scratchLocation=None, allocationProjectNumber=None, resourceSpecificCredentialStoreToken=None,):
    self.computeResourceId = computeResourceId
    self.overridebyAiravata = overridebyAiravata
    self.loginUserName = loginUserName
    self.preferredJobSubmissionProtocol = preferredJobSubmissionProtocol
    self.preferredDataMovementProtocol = preferredDataMovementProtocol
    self.preferredBatchQueue = preferredBatchQueue
    self.scratchLocation = scratchLocation
    self.allocationProjectNumber = allocationProjectNumber
    self.resourceSpecificCredentialStoreToken = resourceSpecificCredentialStoreToken

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.computeResourceId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.overridebyAiravata = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.loginUserName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.preferredJobSubmissionProtocol = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.preferredDataMovementProtocol = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.preferredBatchQueue = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.scratchLocation = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.allocationProjectNumber = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.resourceSpecificCredentialStoreToken = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ComputeResourcePreference')
    if self.computeResourceId is not None:
      oprot.writeFieldBegin('computeResourceId', TType.STRING, 1)
      oprot.writeString(self.computeResourceId)
      oprot.writeFieldEnd()
    if self.overridebyAiravata is not None:
      oprot.writeFieldBegin('overridebyAiravata', TType.BOOL, 2)
      oprot.writeBool(self.overridebyAiravata)
      oprot.writeFieldEnd()
    if self.loginUserName is not None:
      oprot.writeFieldBegin('loginUserName', TType.STRING, 3)
      oprot.writeString(self.loginUserName)
      oprot.writeFieldEnd()
    if self.preferredJobSubmissionProtocol is not None:
      oprot.writeFieldBegin('preferredJobSubmissionProtocol', TType.I32, 4)
      oprot.writeI32(self.preferredJobSubmissionProtocol)
      oprot.writeFieldEnd()
    if self.preferredDataMovementProtocol is not None:
      oprot.writeFieldBegin('preferredDataMovementProtocol', TType.I32, 5)
      oprot.writeI32(self.preferredDataMovementProtocol)
      oprot.writeFieldEnd()
    if self.preferredBatchQueue is not None:
      oprot.writeFieldBegin('preferredBatchQueue', TType.STRING, 6)
      oprot.writeString(self.preferredBatchQueue)
      oprot.writeFieldEnd()
    if self.scratchLocation is not None:
      oprot.writeFieldBegin('scratchLocation', TType.STRING, 7)
      oprot.writeString(self.scratchLocation)
      oprot.writeFieldEnd()
    if self.allocationProjectNumber is not None:
      oprot.writeFieldBegin('allocationProjectNumber', TType.STRING, 8)
      oprot.writeString(self.allocationProjectNumber)
      oprot.writeFieldEnd()
    if self.resourceSpecificCredentialStoreToken is not None:
      oprot.writeFieldBegin('resourceSpecificCredentialStoreToken', TType.STRING, 9)
      oprot.writeString(self.resourceSpecificCredentialStoreToken)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.computeResourceId is None:
      raise TProtocol.TProtocolException(message='Required field computeResourceId is unset!')
    if self.overridebyAiravata is None:
      raise TProtocol.TProtocolException(message='Required field overridebyAiravata is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.computeResourceId)
    value = (value * 31) ^ hash(self.overridebyAiravata)
    value = (value * 31) ^ hash(self.loginUserName)
    value = (value * 31) ^ hash(self.preferredJobSubmissionProtocol)
    value = (value * 31) ^ hash(self.preferredDataMovementProtocol)
    value = (value * 31) ^ hash(self.preferredBatchQueue)
    value = (value * 31) ^ hash(self.scratchLocation)
    value = (value * 31) ^ hash(self.allocationProjectNumber)
    value = (value * 31) ^ hash(self.resourceSpecificCredentialStoreToken)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class DataStoragePreference:
  """
  Attributes:
   - dataMovememtResourceId
   - loginUserName
   - fileSystemRootLocation
   - resourceSpecificCredentialStoreToken
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'dataMovememtResourceId', None, None, ), # 1
    (2, TType.STRING, 'loginUserName', None, None, ), # 2
    (3, TType.STRING, 'fileSystemRootLocation', None, None, ), # 3
    (4, TType.STRING, 'resourceSpecificCredentialStoreToken', None, None, ), # 4
  )

  def __init__(self, dataMovememtResourceId=None, loginUserName=None, fileSystemRootLocation=None, resourceSpecificCredentialStoreToken=None,):
    self.dataMovememtResourceId = dataMovememtResourceId
    self.loginUserName = loginUserName
    self.fileSystemRootLocation = fileSystemRootLocation
    self.resourceSpecificCredentialStoreToken = resourceSpecificCredentialStoreToken

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.dataMovememtResourceId = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.loginUserName = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.fileSystemRootLocation = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.resourceSpecificCredentialStoreToken = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('DataStoragePreference')
    if self.dataMovememtResourceId is not None:
      oprot.writeFieldBegin('dataMovememtResourceId', TType.STRING, 1)
      oprot.writeString(self.dataMovememtResourceId)
      oprot.writeFieldEnd()
    if self.loginUserName is not None:
      oprot.writeFieldBegin('loginUserName', TType.STRING, 2)
      oprot.writeString(self.loginUserName)
      oprot.writeFieldEnd()
    if self.fileSystemRootLocation is not None:
      oprot.writeFieldBegin('fileSystemRootLocation', TType.STRING, 3)
      oprot.writeString(self.fileSystemRootLocation)
      oprot.writeFieldEnd()
    if self.resourceSpecificCredentialStoreToken is not None:
      oprot.writeFieldBegin('resourceSpecificCredentialStoreToken', TType.STRING, 4)
      oprot.writeString(self.resourceSpecificCredentialStoreToken)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.dataMovememtResourceId is None:
      raise TProtocol.TProtocolException(message='Required field dataMovememtResourceId is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.dataMovememtResourceId)
    value = (value * 31) ^ hash(self.loginUserName)
    value = (value * 31) ^ hash(self.fileSystemRootLocation)
    value = (value * 31) ^ hash(self.resourceSpecificCredentialStoreToken)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class GatewayResourceProfile:
  """
  Gateway Resource Profile

  gatewayID:
   Unique identifier for the gateway assigned by Airavata. Corelate this to Airavata Admin API Gateway Registration.

  credentialStoreToken:
   Gateway's defualt credential store token.

  computeResourcePreferences:
   List of resource preferences for each of the registered compute resources.


  Attributes:
   - gatewayID
   - credentialStoreToken
   - computeResourcePreferences
   - dataStoragePreferences
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'gatewayID', None, None, ), # 1
    (2, TType.STRING, 'credentialStoreToken', None, None, ), # 2
    (3, TType.LIST, 'computeResourcePreferences', (TType.STRUCT,(ComputeResourcePreference, ComputeResourcePreference.thrift_spec)), None, ), # 3
    (4, TType.LIST, 'dataStoragePreferences', (TType.STRUCT,(DataStoragePreference, DataStoragePreference.thrift_spec)), None, ), # 4
  )

  def __init__(self, gatewayID=None, credentialStoreToken=None, computeResourcePreferences=None, dataStoragePreferences=None,):
    self.gatewayID = gatewayID
    self.credentialStoreToken = credentialStoreToken
    self.computeResourcePreferences = computeResourcePreferences
    self.dataStoragePreferences = dataStoragePreferences

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.gatewayID = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.credentialStoreToken = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.computeResourcePreferences = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = ComputeResourcePreference()
            _elem5.read(iprot)
            self.computeResourcePreferences.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.dataStoragePreferences = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = DataStoragePreference()
            _elem11.read(iprot)
            self.dataStoragePreferences.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('GatewayResourceProfile')
    if self.gatewayID is not None:
      oprot.writeFieldBegin('gatewayID', TType.STRING, 1)
      oprot.writeString(self.gatewayID)
      oprot.writeFieldEnd()
    if self.credentialStoreToken is not None:
      oprot.writeFieldBegin('credentialStoreToken', TType.STRING, 2)
      oprot.writeString(self.credentialStoreToken)
      oprot.writeFieldEnd()
    if self.computeResourcePreferences is not None:
      oprot.writeFieldBegin('computeResourcePreferences', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.computeResourcePreferences))
      for iter12 in self.computeResourcePreferences:
        iter12.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.dataStoragePreferences is not None:
      oprot.writeFieldBegin('dataStoragePreferences', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.dataStoragePreferences))
      for iter13 in self.dataStoragePreferences:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.gatewayID is None:
      raise TProtocol.TProtocolException(message='Required field gatewayID is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.gatewayID)
    value = (value * 31) ^ hash(self.credentialStoreToken)
    value = (value * 31) ^ hash(self.computeResourcePreferences)
    value = (value * 31) ^ hash(self.dataStoragePreferences)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
