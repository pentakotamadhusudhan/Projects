import 'package:flutter/material.dart';
import 'package:studio/sample.dart';
import 'package:studio/models/post.dart';
import 'package:studio/serivces/remote_service.dart';


// class screen1 extends StatelessWidget{
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: Text('Post a data',style: TextStyle(color: Colors.black87,fontSize: 24),),
//         automaticallyImplyLeading: false,
//         leading: Icon(Icons.menu),
//       ),
//       body:ListView.builder(
//         itemCount:10,
//         itemBuilder: (context,index){
//           return Container(
//
//
//             child: Text('hi...........'),
//           );
//         },
//       ),
//
//     );
//   }
//
// }

class PopupMenuExample extends StatelessWidget {
  const PopupMenuExample({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisSize: MainAxisSize.max,
        children: [
          Container(

            child: Row(

              children: [
                Text('ROW 1'),
                Container(
                  child: Icon(Icons.access_time_filled_sharp,size:100,color: Colors.blue,),
                ),Container(
                  child: Icon(Icons.access_time_filled_sharp,size:100,color: Colors.red,),
                ),
                Container(
                  child: Icon(Icons.access_time_filled_sharp,size:100,color: Colors.yellow,),
                ),
              ],
            )
          ),
          Container(
            width: 200,

            decoration: BoxDecoration(border:Border.all(color: Colors.black87),borderRadius: BorderRadius.circular(20),),
            child: TextButton(onPressed: (){},child: Text('Button'),)
          ),
          Container(
            child: Row(

              children: [
                Text('ROW 2'),
                Container(

                  child: Icon(Icons.add_a_photo,size:100,color: Colors.blue,),
                ),
                Container(
                  child: Icon(Icons.add_a_photo,size:100,color: Colors.red,),
                ),
                Container(
                  child: Icon(Icons.account_circle,size:100,color: Colors.yellow,),
                ),
              ],
            ),
          ),
        ],
      ),


    );
  }
}
