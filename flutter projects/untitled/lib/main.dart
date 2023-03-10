import 'package:flutter/material.dart';
import 'package:untitled/common_screens/screen_1.dart';
import 'package:untitled/common_screens/screen_2.dart';
import 'package:untitled/common_drawer.dart';
import 'package:untitled/common_widgets/drawer_widgets.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import 'package:untitled/search.dart';

var user='madhu';
var pssword = 'Madhu';
List li = [];

void main(){
  return runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: SearchBoxPage(),
    );
  }
}

class myapp extends StatefulWidget {


  const myapp({Key? key}) : super(key: key);

  @override
  State<myapp> createState() => _myappState();
}
// Navigator.push(context,MaterialPageRoute(builder: (context)=>const screen2()),);

class _myappState extends State<myapp> {
  List<dynamic> users = [];
  final TextEditingController _user = TextEditingController();
  final TextEditingController _password = TextEditingController();
  @override
  Widget build(BuildContext context) {
    return Scaffold(


        body: Container(
          padding: EdgeInsets.all(30),
          child:Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          // mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image(image:NetworkImage('https://vivifyassets.s3.ap-south-1.amazonaws.com/cropped-vivify_login.png'),),
            Container(

            child: TextFormField(
              controller: _user,
              decoration: InputDecoration(
                border: UnderlineInputBorder(),
                  labelText: 'user name',
                  labelStyle: TextStyle(
                      color: Colors.black,
                      fontSize: 20)),
              cursorWidth: 2,
            ),
            ),
            Container(
              margin: EdgeInsets.only(top: 20,bottom: 20),
              child: TextField(
                controller: _password,
                obscureText: true,
                obscuringCharacter:'*',
                decoration: InputDecoration(
                    border: UnderlineInputBorder(),
                    labelText: 'Password',
                    labelStyle: TextStyle(
                        color: Colors.black,
                        fontSize: 20)),
                cursorWidth: 2,),
            ),
            ElevatedButton(
                onPressed: (){
                  var x= fetchusers();
                  Navigator.push(context,MaterialPageRoute(builder: (context)=>screen1()),);
                  // login_function();
                  print(_user.text);
                  print(_password.text);
                  if (_user.text==_password.text){
                  li.clear();
                  li.add('');
                  li.add(_password.text);}

                  else{
                    li.clear();
                    li.add('not matched');
                  }
                },
                style: ButtonStyle(backgroundColor:MaterialStatePropertyAll<Color>(Colors.green)),
                child: Text('Login',style: TextStyle(fontSize: 20),))

          ],
        ),
        )
    );
  }
  void fetchusers() async {
    final uri  = Uri.parse('https://jsonplaceholder.typicode.com/posts');
    final response = await http.get(uri);
    // var data = jsonDecode(response.toString());
    if (response.statusCode==200){

      final jsonresponse = jsonDecode(response.body);
      // print(jsonresponse[0]);
      // print(jsonresponse.length);
      var len = jsonresponse.length;
      // li.clear();
      for (var i=0;i<len;i++){
        if (jsonresponse[i]['userId']==9){
          var value =(jsonresponse[i]['id']);

          li.add("Edited On: $value");
    }else if(jsonresponse[i]['userId']==10)
        {
          var value = (jsonresponse[i]['id']);
          li.add('Posted On: $value');
        }
      }
      setState(() {
        users= jsonresponse;
        return jsonresponse;
      });
    }

}}



