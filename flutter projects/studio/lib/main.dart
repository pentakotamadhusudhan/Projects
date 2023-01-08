import 'package:flutter/material.dart';

void main(){
  runApp(MaterialApp(
    home: Myapp()
    )
  )
  ; // runApp
} //main function



// how to show image in screen----
// class Myapp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return  Scaffold(
//       appBar: AppBar(title: Text('Myapp bar'),),
//       body:Center(child: Image(
//         // image: NetworkImage('https://ik.imagekit.io/j83rchiauw/A_List_Star/pawan-kalyan-biography.jpg'),
//       image:AssetImage('assets/img/lifeeazy.jpg'),
//       ))
//     );
//   }
// }


class Myapp extends StatelessWidget {
  var x=' to \n Lifeeazy';
  @override
  Widget build(BuildContext context) {
    return  Scaffold(
        appBar: AppBar(title: Text('Myapp bar'),),
        body:Column(


          children:const <Widget> [
            Center(child: Image(image:AssetImage('assets/img/lifeeazy.jpg'),),),
            // Center(child: Text('welcome',style:TextStyle(fontSize: 40,color: Colors.red,),)),

            // Center(child: Text(x,style:TextStyle(fontSize: 40,color: Colors.red,),)),

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