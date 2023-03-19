// To parse this JSON data, do
//
//     final clinicApiResponseModel = clinicApiResponseModelFromJson(jsonString);

import 'dart:convert';

ClinicApiResponseModel clinicApiResponseModelFromJson(String str) => ClinicApiResponseModel.fromJson(json.decode(str));

String clinicApiResponseModelToJson(ClinicApiResponseModel data) => json.encode(data.toJson());

class ClinicApiResponseModel {
  ClinicApiResponseModel({
    this.message,
    this.result,
    this.hasError,
    this.status,
  });

  final String? message;
  final Result? result;
  final bool? hasError;
  final int? status;

  factory ClinicApiResponseModel.fromJson(Map<String, dynamic> json) => ClinicApiResponseModel(
    message: json["Message"],
    result: json["Result"] == null ? null : Result.fromJson(json["Result"]),
    hasError: json["HasError"],
    status: json["Status"],
  );

  Map<String, dynamic> toJson() => {
    "Message": message,
    "Result": result?.toJson(),
    "HasError": hasError,
    "Status": status,
  };
}

class Result {
  Result({
    this.id,
    this.userId,
    this.offerId,
    this.couponCode,
  });

  final int? id;
  final int? userId;
  final int? offerId;
  final String? couponCode;

  factory Result.fromJson(Map<String, dynamic> json) => Result(
    id: json["id"],
    userId: json["UserId"],
    offerId: json["OfferId"],
    couponCode: json["CouponCode"],
  );

  Map<String, dynamic> toJson() => {
    "id": id,
    "UserId": userId,
    "OfferId": offerId,
    "CouponCode": couponCode,
  };
}
