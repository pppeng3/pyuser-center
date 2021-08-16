import user_center_pb2 as UserCenter
import user_center_pb2_grpc as UserCentergrpc


def Register(request, context):
    response = UserCenter.RegisterResponse()
    return response

def Login(request, context):
    response = UserCenter.LoginResponse()
    return response

def Delete(request, context):
    response = UserCenter.DeleteResponse()
    return response

def CheckToken(request, context):
    response = UserCenter.CheckTokenResponse()
    return response

def Refresh(request, context):
    response = UserCenter.RefreshResponse()
    return response

def GetUserInfo(request, context):
    response = UserCenter.GetUserInfoResponse()
    return response

def AddUser(request, context):
    response = UserCenter.AddUserResponse()
    return response
