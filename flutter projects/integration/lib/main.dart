import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: HomePage(),
    );
  }
}

var StringResponse;
// Map <String, dynamic>mapResponse;
var url_data;

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  Future apicall() async {
    String uri = 'https://reqres.in/api/users/2';
    http.Response response;
    response = await http.get(Uri.parse(uri));
    if (response.statusCode == 200) {
      print('sdfghjkdfghjk ');
      setState(() {
        print(StringResponse);
        StringResponse = response.body;
        var con= jsonDecode(StringResponse);
        // print(StringResponse);
        var data = jsonDecode(StringResponse);
        url_data =(data['data']);
        print(StringResponse.runtimeType);
      });
    }
  }

  @override
  void initState() {
    apicall();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Appbar'),
        ),
        body: Center(
          child: Container(
            height: 200,
            width: 300,
            decoration: BoxDecoration(
                borderRadius: BorderRadius.circular(20), color: Colors.cyan),
            child: Center(
              child: Text(StringResponse.toString()),
            ),
          ),
        ));
  }
}
