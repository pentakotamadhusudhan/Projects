import 'package:flutter/material.dart';
import 'package:studio/views/doctor_screen.dart';
import 'package:studio/views/registrationscreen.dart';


void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: _myapp(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class _myapp extends StatefulWidget {
  const _myapp({Key? key}) : super(key: key);

  @override
  State<StatefulWidget> createState() {
    return _mystateless();
  }
}

class _mystateless extends State<_myapp> {
  TextEditingController _username = TextEditingController();
  TextEditingController _password = TextEditingController();
  var username = 'Madhu';
  var password = 'password';
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        children: [
          Container(
            padding: EdgeInsets.only(top: 50),
            child: Image(image: NetworkImage('https://www.vivifyhealthcare.com/wp-content/uploads/2021/02/cropped-vivify_login.png'),),
          ),
          Container(
            padding: EdgeInsets.only(top:20,left: 30,right: 30),
            child: TextField(decoration: InputDecoration(labelText: 'UserName'),
            controller: _username,
            ),
          ),
          Container(
            padding: EdgeInsets.only(top:10,left: 30,right: 30),
            child: TextField(decoration: InputDecoration(labelText: 'Password'),
            controller: _password,
              ),
          ),
          Container(

            child: Row(
              children: [
                Container(
                  padding: EdgeInsets.only(left: 30,),
                  child: Text('Not Signed up yet?'),
                ),
                TextButton(
                    onPressed: (){
                      Navigator.push(
                        context,
                        MaterialPageRoute(builder: (madhu) =>  regiScreen()),
                      );
                    },

                    child: Text('Register')
                ),
              ],
            ),
          ),
          Container(

            padding: EdgeInsets.only(top: 25),
            child: ElevatedButton(onPressed: (){
              Icon(Icons.menu);
              // print(_username.text);
              // print(_password.text);
              if (username==_username.text){
                Navigator.push(
                  context,
                  MaterialPageRoute(builder: (madhu) =>  typeofpartners()),
                );
                print('ohk');
                if (password==_password.text){
                  print('Login sucecss');
                }
              }

            }, child: Text('Login')),
          ),
        ],
      ),
    );

  }
}






class NavDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: <Widget>[
          DrawerHeader(
            child: Text(
              'Side menu',
              style: TextStyle(color: Colors.white, fontSize: 25),
            ),
            decoration: BoxDecoration(
                color: Colors.green,
                image: DecorationImage(
                    fit: BoxFit.fill,
                    image: AssetImage('assets/images/cover.jpg'))),
          ),
          ListTile(
            leading: Icon(Icons.input),
            title: Text('Welcome'),
            onTap: () => {},
          ),
          ListTile(
            leading: Icon(Icons.verified_user),
            title: Text('Profile'),
            onTap: () => {Navigator.of(context).pop()},
          ),
          ListTile(
            leading: Icon(Icons.settings),
            title: Text('Settings'),
            onTap: () => {Navigator.of(context).pop()},
          ),
          ListTile(
            leading: Icon(Icons.border_color),
            title: Text('Feedback'),
            onTap: () => {Navigator.of(context).pop()},
          ),
          ListTile(
            leading: Icon(Icons.exit_to_app),
            title: Text('Logout'),
            onTap: () => {Navigator.of(context).pop()},
          ),
        ],
      ),
    );
  }
}