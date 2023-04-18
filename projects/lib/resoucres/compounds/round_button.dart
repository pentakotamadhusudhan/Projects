import 'package:flutter/material.dart';
import 'package:projects/resoucres/compounds/color.dart';

class RoundButton extends StatelessWidget {


  final String title ;
  final bool loading ;
  final VoidCallback onPress ;


  const RoundButton({Key? key,
  required this.title,
  this.loading=false,
  required this.onPress,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {

    return InkWell(
      onTap: onPress,
      child: Container(
        height: 30,
        width: 100,
        decoration: BoxDecoration(
          color: AppColors.buttoncolor,
          borderRadius: BorderRadius.circular(20)
        ),
        child: Center(child:loading?  Text("Button"): CircularProgressIndicator(color: AppColors.Blackcolor,strokeWidth: 2.0,) ),
      ),
    );
  }
}

