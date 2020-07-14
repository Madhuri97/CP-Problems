// You can use this class to represent how classy someone
// or something is.
// "Classy" is interchangable with "fancy".
// If you add fancy-looking items, you will increase
// your "classiness".
// Create a function in "Classy" that takes a string as
// input and adds it to the "items" list.
// Another method should calculate the "classiness"
// value based on the items.
// The following items have classiness points associated
// with them:
// "tophat" = 2
// "bowtie" = 4
// "monocle" = 5
// Everything else has 0 points.
// Use the test cases below to guide you!

import java.util.*;


public class Classy {
    ArrayList<String> items = new ArrayList<>();
    // String s;
    int addItem = 0; 
    public void addItem(String s) {
        items.add(s);
    }
    public int classiness() {
        for(String item:items) {

            if(item.equals("tophat")){
                addItem += 2;
            }
            if(item.equals("bowtie")){
                addItem += 4;
            }
            if(item.equals("monocle")) {
                addItem += 5;
            } else {
                addItem += 0;
            }
        } 
        return addItem;
    }
    public static void main(String[] args) {
        
    }
}
