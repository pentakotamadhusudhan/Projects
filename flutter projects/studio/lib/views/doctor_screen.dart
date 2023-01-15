import 'package:flutter/material.dart';
import 'package:studio/sample.dart';
import 'package:studio/models/post.dart';
import 'package:studio/serivces/remote_service.dart';


class screen1 extends StatelessWidget{

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Post a data',style: TextStyle(color: Colors.black87,fontSize: 24),),
        automaticallyImplyLeading: false,
        leading: Icon(Icons.menu),
      ),
      body:ListView.builder(
        itemCount:10,
        itemBuilder: (context,index){
          return Container(


            child: Text('hi...........'),
          );
        },
      ),

    );
  }

}