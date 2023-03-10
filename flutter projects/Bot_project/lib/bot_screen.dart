
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


