void main() {
  List listA = [
    "Muklah",
    "Diyar",
    "Noorhan",
    "Ali",
    "Abdulbasit",
    "Dena",
    "Saba",
    "Fadi",
    "Karrar",
    "Ahmed"
  ];
  List listB = [
    "Diyar",
    "Noorhan",
    "Muklah",
    "Saba",
    "Mustafa",
    "Ahmed",
    "Fadi",
    "Dena",
    "Hassan",
    "Ali",
  ];
  List common = [];
  for (final i in listA) {
    for (final j in listB) {
      if (i == j) {
        common.add(i);
      }
    }
  }

  print(common);
  List listM = [];
  for (final n in listA) {
    for (final v in listB) {
      if (n == 'Ahmed' || n == 'Muklah' || n == 'Mustafa') {
        listM.add(n);
      }
    }
  }
}
