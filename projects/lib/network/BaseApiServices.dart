

abstract class BaseApiServices{
  Future<dynamic> getGetApiResponse(String url,Map<String,String>header);
  Future<dynamic> getPostApiResponse(String url,Map<String,String>header,dynamic data);

}