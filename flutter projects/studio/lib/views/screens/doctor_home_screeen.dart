import 'package:flutter/material.dart';

class doctor_home_screen extends StatefulWidget {
  const doctor_home_screen({Key? key}) : super(key: key);

  @override
  State<doctor_home_screen> createState() => _doctor_home_screenState();
}




class _doctor_home_screenState extends State<doctor_home_screen> {
  @override

  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(

        backgroundColor: Colors.white,
        shadowColor: Colors.blue,
        // leading: IconButton(icon: ImageIcon(NetworkImage('https://www.pngitem.com/pimgs/m/20-203432_profile-icon-png-image-free-download-searchpng-ville.png')),onPressed: (){},iconSize: 100,),
        leading: Icon(Icons.menu),
        foregroundColor: Colors.blue,
        toolbarHeight: 150,
        actions: [
          Column(children:[Row(children: [
            Image(image: NetworkImage('https://www.vivifyhealthcare.com/wp-content/uploads/2021/02/cropped-vivify_login.png')),
            IconButton(onPressed: (){}, icon:Icon(Icons.notifications_outlined,color: Colors.black,)),
          ],
          ),
            Container(

              
              child:Row(children: [
                Icon(Icons.pin_drop_outlined,color: Colors.black,),
                Text('data',style: TextStyle(color: Colors.black),),
                Icon(Icons.arrow_drop_down_outlined,color: Colors.black,),
              ],),
            )
            
          ],
            
    ),
          
        ],

        ),


      );

  }
}
