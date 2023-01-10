import 'package:flutter/material.dart';

void main(){
  runApp(MaterialApp(
    home: Myapp()
    )
  )
  ; // runApp
} //main function



// how to show image in screen----



class Myapp extends StatelessWidget {
  var x=' to \n Lifeeazy';
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
        appBar: AppBar(title: Text('Myapp bar'),),
        body:Column(


          children:const <Widget> [
            Center(child: Image(image:AssetImage('assets/img/lifeeazy.jpg'),),),
          Center(child: Center(child: TextField(decoration: InputDecoration(labelText: "User Name",),),),
        ),

            Center(
                child: Center(child: TextField(decoration: InputDecoration(labelText: "Password",hintText: 'enter your password'),),),
              ),

            ElevatedButton(onPressed: func,
            child: Text('Login',
            style: TextStyle(color: Colors.yellow,fontSize: 30,backgroundColor: Colors.blueAccent),
            ),
            )


          ],
        )
    );
  }
}

func(){
  print(200);
}