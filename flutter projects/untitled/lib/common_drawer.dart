import 'package:flutter/material.dart';

class mydrawer extends StatelessWidget {
  // const mydrawer({Key? key}) : super(key: key);
  final Widget draw_widget;

  mydrawer({
    required this.draw_widget,


  });
  @override
  Widget build(BuildContext context) {
    return Drawer(
      width: 200,
      child:SizedBox(
        width: 10,
        child:draw_widget,
      )
    );
  }

}
