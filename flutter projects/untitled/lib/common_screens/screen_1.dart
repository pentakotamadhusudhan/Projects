import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:untitled/common_drawer.dart';
import 'package:untitled/common_widgets/drawer_widgets.dart';
import 'package:untitled/main.dart';
import 'package:http/http.dart' as http;
import 'package:untitled/model/user_model.dart';
import 'package:untitled/common_screens/chat_screen.dart';
import 'package:untitled/model/user_model.dart';


var boddy = '';
class screen1 extends StatefulWidget {
  // final Post post;

  // const screen1({Key? key, required this.post}) : super(key: key);

  @override
  State<screen1> createState() => _screen1State();
}

class _screen1State extends State<screen1> {
  List<dynamic> users=[];
  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(title: Text('screen 1'),),
      drawer:mydrawer(draw_widget: drew_widget1(context),) ,
      body:ListView.builder(
        itemCount: li.length,
          itemBuilder: (context,index){
        return Column(
          children: [
            Chat_screen(),

            Text("post data "),
            Text("post data ")
          ],
        );
      }),
      );

  }
}
