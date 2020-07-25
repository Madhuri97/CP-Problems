/**
 * This is JUnit that tests the methods of the Clock.
 * This contains 2 testcases.
 * 
 * Please don't run this file.
 * You can add your own test cases to this file by just copy and 
 * paste the last three lines of the code (TestCase2).
 * 
 * @author: Deepak
 */

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.beans.Transient;

public class TestJUnit {

   @Test
   public void testCase1() {
      largestnumber s = new largestnumber();
      
      assertEquals("1.", 32, s.fun_largestnumber("we have 32 dogs 3 cats"));
      assertEquals("2.", 0, s.fun_largestnumber("we have dogs cats"));
   }

   @Test
   public void testCase2() {
      largestnumber s = new largestnumber();
      
      assertEquals("1.", 17, s.fun_largestnumber("I saw 3 dogs, 17 cats, and 14 cows!"));
      assertEquals("2.", 15, s.fun_largestnumber("wehave15dogs2cats"));
   }
}

