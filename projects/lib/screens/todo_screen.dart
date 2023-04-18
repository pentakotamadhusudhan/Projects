import 'package:flutter/material.dart';
import 'package:projects/utils/utils.dart';
import 'package:projects/resoucres/compounds/round_button.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  State<LoginScreen> createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  TextEditingController _username = TextEditingController();
  TextEditingController _password = TextEditingController();

  FocusNode usernamefocusnode = FocusNode();
  FocusNode passwordfocusnode = FocusNode();

  ValueNotifier<bool> _obsecurepassword = ValueNotifier(true);

  @override
  Widget build(BuildContext context) {
    final height = MediaQuery.of(context).size.height*1;


    return Scaffold(
        body: Container(

      decoration: BoxDecoration(
          image: DecorationImage(
              image: NetworkImage(
                  "https://w0.peakpx.com/wallpaper/948/162/HD-wallpaper-minato-anime-naruto-hokage.jpg"),
              fit: BoxFit.fitWidth)),
      child: Padding(
        padding: const EdgeInsets.all(50.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            TextFormField(
              controller: _username,
              keyboardType: TextInputType.emailAddress,
              focusNode: usernamefocusnode,
              decoration: InputDecoration(
                prefixIcon: Icon(Icons.email_rounded),
                labelText: "User Name",
                labelStyle: TextStyle(color: Colors.white),
              ),
              onFieldSubmitted: (value){
                // FocusScope.of(context).requestFocus(passwordfocusnode);
                utilsclass.fieldFocusChange(context, usernamefocusnode, passwordfocusnode);
              },
            ),
            ValueListenableBuilder(valueListenable: _obsecurepassword, builder: (context,value, chlid){
              return TextFormField(
                controller: _password,
                obscureText: _obsecurepassword.value,
                obscuringCharacter: "#",
                focusNode: passwordfocusnode,
                decoration: InputDecoration(
                  prefixIcon: Icon(Icons.lock),
                  suffixIcon: InkWell(
                      onTap: (){
                        _obsecurepassword.value =! _obsecurepassword.value;
                      },
                      child:_obsecurepassword.value?Icon(Icons.visibility_off_sharp):(Icon(Icons.remove_red_eye_rounded))),
                  labelText: "Password",
                  labelStyle: TextStyle(color: Colors.white,fontSize: 20),

                ),
                onTap: (){
                  // FocusScope.of(context).requestFocus(usernamefocusnode);
                  utilsclass.fieldFocusChange(context, passwordfocusnode, usernamefocusnode);

                },
              );
            }),
            SizedBox(height: height*0.03,),
            RoundButton(
              title:'madhu',
              loading: true,
              onPress: (){
                print(_username.text);
                print(_password.text);
                if(_username.text.length<=0){
               ScaffoldMessenger.of(context).showSnackBar(
                   SnackBar(backgroundColor: Colors.red,
                     content: Text("Error message",style: TextStyle(color: Colors.white),),)

               );}
              },
            ),
           ],
        ),
      ),
    ));
  }
}
