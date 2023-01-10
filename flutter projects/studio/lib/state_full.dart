import 'package:flutter/material.dart';

MyApp main(){
  return MyApp();
}

class MyApp  extends StatefulWidget {

  @override
  State<StatefulWidget> createState() {
    return _myapp();
  }

}

class _myapp extends State<MyApp>{
  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        Container(
          child: TextField(decoration: InputDecoration(labelText: "username"),),
        ),
      ],
    );
  }
}