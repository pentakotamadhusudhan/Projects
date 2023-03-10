import 'package:flutter/material.dart';
import 'package:untitled/main.dart';

Widget drew_widget_main(BuildContext context) {
  return ListView(children: [
    ListTile(
      title: Text('tile1text'),
    ),
    ListTile(
      title: Text('tile2text'),
    ),
    ListTile(
      title: Text('tile3text'),
    ),
    ListTile(
      title: Text('tile4text'),
    ),
    ListTile(
      title: Text('tile5text'),
    ),
    ListTile(title: Text("Logout"),
    onTap: (){
      Navigator.push(context,MaterialPageRoute(builder: (context)=>const myapp()),);

    },)
  ]);
}

Widget drew_widget1(BuildContext context) {
  return ListView(children: [
    ListTile(
      title: Text('screen 1'),
    ),
    ListTile(
      title: Text('screen 1'),
    ),
    ListTile(
      title: Text('screen 1'),
    ),
    ListTile(
      title: Text('tile4text'),
    ),
    ListTile(
      title: Text('tile5text'),
    ),
    ListTile(title: Text("Logout"),
      onTap: (){
        Navigator.push(context,MaterialPageRoute(builder: (context)=>const myapp()),);

      },)
  ]);
}

Widget drew_widget2(BuildContext context) {
  return ListView(children: [
    ListTile(
      title: Text('screen 3'),
    ),
    ListTile(
      title: Text('screen 3'),
    ),
    ListTile(
      title: Text('tile3text'),
    ),
    ListTile(
      title: Text('tile4text'),
    ),
    ListTile(
      title: Text('tile5text'),
    ),
    ListTile(title: Text("Logout"),
      onTap: (){
        Navigator.push(context,MaterialPageRoute(builder: (context)=>const myapp()),);

      },)
  ]);
}
