// import 'package:flutter/material.dart';
//
//
// import 'dart:convert';
// import 'package:bubble/bubble.dart';
// import 'package:flutter/material.dart';
// import 'package:http/http.dart' as http;
//
// class Bot_screen extends StatefulWidget {
//   const Bot_screen({Key? key}) : super(key: key);
//
//   @override
//   State<Bot_screen> createState() => _Bot_screen();
// }
//
//
// class _Bot_screen extends State<Bot_screen> {
//   final ScrollController _scrollController = ScrollController();
//   final GlobalKey<AnimatedListState> _listkey = GlobalKey();
//   List<String> _data = [];
//   // static const String Bot_URL = 'http://bot.vivifyhealthcare.com:5006/webhooks/rest/webhook';
//   String Bot_URL= 'http://bot.vivifyhealthcare.com:5007/webhooks/rest/webhook';
//
//   TextEditingController querycontroller = TextEditingController();
//
//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       backgroundColor: Colors.blueAccent[100],
//       appBar: AppBar(
//         centerTitle: true,
//         backgroundColor: Colors.blueAccent,
//         title: Text('chat bot'),),
//       body: Stack(
//         children: <Widget>[
//           AnimatedList(
//             key: _listkey,
//             itemBuilder: (BuildContext context, int index,
//                 Animation animation) {
//               return buildItem(_data[index], animation, index);
//             },
//           ),
//           Align(
//             alignment: Alignment.bottomCenter,
//             child: ColorFiltered(
//               colorFilter: ColorFilter.linearToSrgbGamma(),
//               child: Container(
//                 color: Colors.white,
//                 child: Padding(
//                   padding: EdgeInsets.only(left: 20, right: 20),
//                   child: TextField(
//
//                     controller: querycontroller,
//                     textInputAction: TextInputAction.send,
//                     onSubmitted: (msg) {
//                       this.getrespose(msg);
//                       querycontroller.clear();
//                     },
//                     decoration: InputDecoration(icon: Icon(Icons.message),
//                         hintText: 'enter ur message'),
//
//                   ),
//                 ),
//               ),
//             ),
//           )
//         ],
//       ),
//
//     );
//   }
//
//   List response_list = [];
//
//   getrespose(msg) async {
//     insertSingleItem(msg);
//
//     var client = http.Client();
//     var url = Uri.parse(Bot_URL);
//     var data_message = jsonEncode({"message":msg,"sender":"llll"});
//     var response = await client.post(url, body: data_message);
//     print(response.statusCode);
//     print("------ ${response.body}");
//     // print(jsonDecode(response.body));
//     // print((jsonDecode(response.body)).length);
//     int len_respo = (( (response.body)).length);
//     // print(len_respo);
//     var respo = jsonDecode(response.body);
//     // print(respo.runtimeType);
//     // print(respo);
//
//
//     for (int i = 0; i < len_respo; i++) {
//       Map<String, dynamic> x = respo[i];
//       bool y = respo[i]['image'] != null;
//       bool b = respo[i]['buttons'] != null;
//       bool d = respo[i]['text'] != null;
//       if(d=true){
//         if (respo[i]['text'].toString().startsWith('http')) {
//           response_list.add(respo[i]['text'].toString() + '<bot>');
//           insertSingleItem('url'+respo[i]['text'].toString() + "<bot>");
//           // print(m);
//         }
//       }
//       if (b == true) {
//         List mm = respo[i]['buttons'];
//         // insertSingleItem(respo[i]['buttons'].toString() + "<bot>");
//         int mm_len = mm.length;
//         bool m = respo[i]['text'] != null;
//         response_list.add(respo[i]['text'].toString() + '<bot>');
//         insertSingleItem(respo[i]['text'].toString() + "<bot>");
//         // print(m);
//         for (int j = 0; j < mm_len; j++) {
//           // print(respo[i]['button'][j].runtimeType);
//           response_list.add(respo[i]['buttons'][j].toString() + '<bot>');
//           insertSingleItem("@"+respo[i]['buttons'][j]['title'].toString() + "<bot>");
//           // insertSingleItem(respo[i]['buttons'][j]['title'].toString() + "<bot>");
//           // insertSingleItem(respo[i]['buttons'][j]['payload'].toString() + "<bott>");
//         }
//         bool d = respo[i]['text'] != null;
//       } else if (y == true) {
//         response_list.add(respo[i]['image'].toString() + '<bot>');
//         insertSingleItem(respo[i]['image'].toString() + "<bot>");
//       } else if (d != null) {
//
//         response_list.add(respo[i]['text'].toString() + '<bot>');
//         insertSingleItem(respo[i]['text'].toString() + "<bot>");
//       }
//     }
//
//     int nn = response_list.length;
//     print(response_list);
//     for (int h = 0; h < nn; h++) {
//       print("boooo --- ${response_list[h]}");
//     }
//     response_list.clear();
//   }
//
//   void insertSingleItem(String mes) {
//     _data.add(mes);
//     _listkey.currentState?.insertItem(_data.length - 1);
//   }
//
//   http.Client getclient() {
//     return http.Client();
//   }
//
//
//   Widget buildItem(String item, animation, int index) {
//     // List url_button =
//
//     bool img = item.startsWith('http');
//     bool mine = item.endsWith('<bot>');
//
//
//     return Scrollbar(
//         thickness: 10, //width of scrollbar
//         radius: Radius.circular(20), //corner radius of scrollbar
//         scrollbarOrientation: ScrollbarOrientation.top,
//         child: SizeTransition(sizeFactor: animation,
//           child: Padding(padding: EdgeInsets.all(10),
//             child: Container(
//               alignment: mine ? Alignment.topLeft : Alignment.topRight,
//               child: Bubble(
//                 // child:img? Image(image: NetworkImage(item.replaceAll('<bot>', ''))):Text(item.replaceAll('<bot>', ""),style: TextStyle(color: Colors.white)),
//                 child: madhu(item,index),
//                 color: mine ? Colors.black : Colors.blue,
//                 padding: BubbleEdges.all(10),
//               ),
//             ),
//           ),
//         ));
//   }
//
//
//   Widget madhu(item,index) {
//     bool img = item.startsWith('https');
//     bool mine = item.endsWith('<bot>');
//     bool btn = item.startsWith('@');
//     bool txt = item.startsWith('/');
//
//
//     if (img == true) {
//       return Image(image: NetworkImage(item.replaceAll('<bot>', '')));
//     }
//     else if(btn==true){
//       var btn_text = item.replaceAll('@','');
//       var btn_text2 = (btn_text.replaceAll('<bot>',''));
//       print(btn_text2);
//       if (txt==false) {
//         return ElevatedButton(onPressed: () {
//           var btn_text3 = _data[index];
//           // insertSingleItem(btn_text3.replaceAll("<bot>", ''));
//
//           getrespose(btn_text3.replaceAll("<bot>", ''));
//           print(btn_text3.replaceAll("<bot>", ''));
//         },
//             child: Text(btn_text2, style: TextStyle(color: Colors.black),));
//       }else{
//         print('object');
//         return Text('');
//       }
//     }
//     else  {
//       if(txt==false) {
//         return Text(
//           item.replaceAll('<bot>', ''), style: TextStyle(color: Colors.white),);
//       }else if(txt==true){
//         var btn_text = item.replaceAll('url','');
//         var btn_text2 = (btn_text.replaceAll('<bot>',''));
//         return ElevatedButton(onPressed: () {
//           var btn_text3 = _data[index];
//           insertSingleItem(btn_text3 + "<bot>");
//
//           getrespose(btn_text3.replaceAll("<bot>", ''));
//           print(btn_text3.replaceAll("<bot>", ''));
//         },
//             child: Text(btn_text2, style: TextStyle(color: Colors.black),));
//
//       }
//       else{
//         return Text(item.replaceAll('<bot>', ''),style: TextStyle(color: Colors.white),);
//       }
//     }
//   }
//
//
//
// }




import 'dart:convert';
import 'package:bubble/bubble.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

class Bot_screen extends StatefulWidget {
  const Bot_screen({Key? key}) : super(key: key);

  @override
  State<Bot_screen> createState() => screenState();
}

class screenState extends State<Bot_screen> {
  final GlobalKey<AnimatedListState> _listkey = GlobalKey();
  final ScrollController _scrollController = ScrollController(
    initialScrollOffset: 0.0,


  );
  bool _needsScroll = false;


  List<String> _data = [];
  double _amountToScroll(){
return 0.10;
  }
  static const String Bot_URL =
      'http://bot.vivifyhealthcare.com:5007/webhooks/rest/webhook';
  TextEditingController querycontroller = TextEditingController();

void initState() {
  // getrespose('msg');
}


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        centerTitle: true,
        backgroundColor: Colors.white,
        foregroundColor: Colors.black,
        title: const Text('Chat Bot'),
      ),
      body: Stack(
        children: <Widget>[

   AnimatedList(
     scrollDirection: Axis.vertical,
        padding: EdgeInsetsDirectional.only(bottom: 50.0),
        key: _listkey,
        itemBuilder: (BuildContext context, int index, Animation animation) {
          return buildItem(_data[index], animation, index);

        },
      ),
          Align(
           alignment: Alignment.bottomCenter,
           child: ColorFiltered(
             colorFilter: const ColorFilter.linearToSrgbGamma(),
             child: Container(
               color: Colors.white,
               child: Padding(
                 padding: const EdgeInsets.only(left: 20, right: 20),
                 child: TextField(
                   controller: querycontroller,
                   textInputAction: TextInputAction.send,
                   onSubmitted: (msg) {
                     this.getrespose(msg);
                     querycontroller.clear();
                   },
                   decoration: const InputDecoration(
                       icon: Icon(Icons.message),
                       hintText: 'enter ur message'),
                 ),
               ),
             ),
           ),
         )
        ],
      ),
    );
  }

  List response_list = [];

  getrespose(msg) async {
    print('--------------------------- msg ------------- $msg');
    insertSingleItem(msg.replaceAll('@', ''));

    var client = http.Client();
    var url = Uri.parse(Bot_URL);
    var dataMessage = jsonEncode({'message': msg});
    var response = await client.post(url, body: dataMessage);
    print(response.statusCode);
    print(jsonDecode(response.body));

    int lenRespo = ((jsonDecode(response.body)).length);

    var respo = jsonDecode(response.body);

    for (int i = 0; i < lenRespo; i++) {
      bool y = respo[i]['image'] != null;
      bool b = respo[i]['buttons'] != null;
      bool d = respo[i]['text'] != null;
      if (b == true) {
        List mm = respo[i]['buttons'];

        int mmLen = mm.length;
        response_list.add('${respo[i]['text']}<bot>');
        insertSingleItem("${respo[i]['text']}<bot>");

        for (int j = 0; j < mmLen; j++) {
          response_list.add('${respo[i]['buttons'][j]}<bot>');
          insertSingleItem("@${respo[i]['buttons'][j]['title']}<bot>");
        }
      } else if (y == true) {
        response_list.add('${respo[i]['image']}<bot>');
        insertSingleItem("${respo[i]['image']}<bot>");
      } else if (d != null) {
        response_list.add('${respo[i]['text']}<bot>');
        insertSingleItem("${respo[i]['text']}<bot>");
      }
    }

    response_list.clear();
  }

  void insertSingleItem(String mes) {
    _data.add(mes);
    _listkey.currentState?.insertItem(_data.length - 1);
  }

  http.Client getclient() {
    return http.Client();
  }

  Widget buildItem(String item, animation, int index) {
    bool mine = item.endsWith('<bot>');

    return
         Container(

            child: Padding(
              padding: const EdgeInsets.all(10),
              child: Container(
                  alignment: mine ? Alignment.topLeft : Alignment.topRight,
                  child: mine
                      ? Container(
                    // child:img? Image(image: NetworkImage(item.replaceAll('<bot>', ''))):Text(item.replaceAll('<bot>', ""),style: TextStyle(color: Colors.white)),
                    child: madhu(item, index),
                    color: mine ? Colors.white : Colors.blue,
                  )
                      : Bubble(
                    alignment: Alignment.topRight,
                    color: Colors.white,
                    child: madhu(item, index),
                  )),
            ));
  }

  Widget madhu(item, index) {
    bool img = item.startsWith('https');
    bool btn = item.startsWith('@');
    bool txt = item.startsWith('/');

    if (img == true) {
      return Image(image: NetworkImage(item.replaceAll('<bot>', '')));
    } else if (btn == true) {
      var btnText = item.replaceAll('@', '');
      var btnText2 = (btnText.replaceAll('<bot>', ''));
      print(btnText2);
      if (txt == false) {
        return ElevatedButton(
          onPressed: () {
            var btnText3 = _data[index];
            getrespose(btnText3.replaceAll("<bot>", ''));
            print(btnText3.replaceAll("<bot>", ''));
          },
          child: Text(
            btnText2,
            style: const TextStyle(color: Colors.black),
          ),
          style: ElevatedButton.styleFrom(primary: Colors.blue[500]),
        );
      } else {
        print('object');
        return const Text('');
      }
    } else {
      return Text(
        item.replaceAll('<bot>', ''),
        style:
        const TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
      );
    }
  }


}


