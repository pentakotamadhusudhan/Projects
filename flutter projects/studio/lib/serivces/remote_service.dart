import 'package:studio/models/Post.dart';
import 'package:http/http.dart' as http;

class RemoteSerivce{
  Future<List<Post?>?> getPosts() async{
    var client = http.Client();
    var uri = Uri.parse('https://jsonplaceholder.typicode.com/posts');
    var response = await client.get(uri);
    if (response.statusCode==200){
      var json = response.body;
      var x= postFromJson(json);
      return x;

    }

  }
}