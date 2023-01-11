import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: _myapp(),
    );
  }
}

class _myapp extends StatefulWidget {
  const _myapp({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() {
    return _mystateless();
  }
}

class _mystateless extends State<_myapp> {
  TextEditingController _username = TextEditingController();
  TextEditingController _password = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [

          Container(
            padding: EdgeInsets.only(top:200,left: 30,right: 30),
            child: TextField(decoration: InputDecoration(labelText: 'UserName'),
            controller: _username,
            ),
          ),
          Container(
            padding: EdgeInsets.only(top:10,left: 30,right: 30),
            child: TextField(decoration: InputDecoration(labelText: 'Password'),
            controller: _password,
              ),
          ),
          Container(
            padding: EdgeInsets.only(top: 10),
            child: ElevatedButton(onPressed: (){
              print(_username.text);
              print(_password.text);
            }, child: Text('button')),
          ),
        ],
      ),
    );

  }
}