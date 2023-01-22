import 'dart:convert';
import 'dart:async';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
 List<dynamic> users =[];
 void fetchUsers() async{

   final uri = Uri.parse('https://randomuser.me/api/?results=5000');
   await http.get(uri);
   final response = await(http.get(uri));
   final body = response.body;
   final code = response.hashCode;
   final json = jsonDecode(body);
   setState((){
     users = json['resluts'];
   });
   print('fetch functon called');
 }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('app bar'),
      ),
      body: ElevatedButton(onPressed: fetchUsers,
        child: Text('button'),),
    );
  }
}








