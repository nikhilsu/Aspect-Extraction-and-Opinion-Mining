package edu.bigdata.kafkaspark;

class Tuple<X, Y> {
    final X x;
    final Y y;

    Tuple(X x, Y y) {
        this.x = x;
        this.y = y;
    }
}
