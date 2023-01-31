import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

import static java.lang.Math.sqrt;

public class Controll implements Runnable {
    private boolean on_off;
    private Blinky myB;
    private Clyde myC;
    private Pacman myP;
    private Pinky myPinky;
    private View myN;
    private Inky inky;
    private Main main;
    private SoundControl sc;
    private ArrayList<Integer> list;
    private int mode = 1;

    public boolean isOn_off() {
        return on_off;
    }

    public void setOn_off(boolean on_off) {
        this.on_off = on_off;
    }

    public Blinky getMyB() {
        return myB;
    }

    public void setMyB(Blinky myB) {
        this.myB = myB;
    }

    public Clyde getMyC() {
        return myC;
    }

    public void setMyC(Clyde myC) {
        this.myC = myC;
    }

    public Pacman getMyP() {
        return myP;
    }

    public void setMyP(Pacman myP) {
        this.myP = myP;
    }

    public Pinky getMyPinky() {
        return myPinky;
    }

    public void setMyPinky(Pinky myPinky) {
        this.myPinky = myPinky;
    }

    public View getMyN() {
        return myN;
    }

    public void setMyN(View myN) {
        this.myN = myN;
    }

    public Inky getInky() {
        return inky;
    }

    public void setInky(Inky inky) {
        this.inky = inky;
    }

    public Controll(Blinky myB, View myN, Pacman p, Clyde myC, Pinky myPinky, Inky inky, Main main, ArrayList<Integer> list) throws InterruptedException, FileNotFoundException {
        this.myC = myC;
        this.myB = myB;
        this.myN = myN;
        myP = p;
        this.myPinky = myPinky;
        this.inky = inky;
        on_off = true;
        this.main = main;
        sc = new SoundControl();
        this.list = list;
    }

    @Override
    public void run() {
        if (list.size() % 3 != 0) {
            System.out.println("Wrong path!");
            on_off = false;
        }
        int i = 0;
        try {
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        int pathIndex = 0;
        int pathX;
        int pathY;
        int pathDir;
        if(list.size() >= (pathIndex * 3 + 3) && mode == 1) {
            pathX = list.get(pathIndex * 3);
            pathY = list.get(pathIndex * 3 + 1);
            pathDir = list.get(pathIndex * 3 + 2);
            pathIndex++;
        } else {
            pathX = 0;
            pathY = 0;
            pathDir = 0;
            if(mode == 1) {
                on_off = false;
            }
        }

        while (on_off) {
            //System.out.println("X: " + myP.getX() + " Y: " + myP.getY());
            //System.out.println(myB.getDirection());
            myB.move();
            myP.move();
            myC.move();
            myPinky.move();
            inky.move();

            if(myP.getX() == pathY*20 && myP.getY() == pathX*20) {
                myP.setDirection(pathDir);

                if(list.size() >= (pathIndex * 3 + 3) && mode == 1) {
                    pathX = list.get(pathIndex * 3);
                    pathY = list.get(pathIndex * 3 + 1);
                    pathDir = list.get(pathIndex * 3 + 2);
                    pathIndex++;
                }
            }

            try {
                Thread.sleep(10);
            } catch (InterruptedException e) {
                System.out.println("Thread.sleep error!");
            }
            myN.repaint();
            i++;
            int ind = myP.checkRec();
            if (ind != -1) {
                sc.eat();
                myN.setLevel((short) 10, ind);
                myN.setPoint(myN.getPoint() + 10);
            }
            int ind2 = myP.checkCirc();
            if (ind2 != -1) {
                sc.eatCirc();
                myN.setLevel((short) 10, ind2);
                myB.setMode(3);
                myC.setMode(3);
                myPinky.setMode(3);
                inky.setMode(3);
            }
            if (myB.gotya(myP.getX(), myP.getY())) {
                if (myP.getLife() > 1) {
                    myP.setLife(myP.getLife() - 1);
                    myP.setX(280);
                    myP.setY(340);
                    myB.setY(100);
                    myB.setX(100);
                    myPinky.setX(420);
                    myPinky.setY(100);
                    inky.setX(420);
                    inky.setY(580);
                    myC.setX(100);
                    myC.setY(580);
                    try {
                        Thread.sleep(2000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                } else {
                    on_off = false;
                }
            }
//            if (myPinky.gotya(myP.getX(), myP.getY())) {
//                if (myP.getLife() > 1) {
//                    myP.setLife(myP.getLife() - 1);
//                    myP.setX(280);
//                    myP.setY(340);
//                    myB.setY(100);
//                    myB.setX(100);
//                    myPinky.setX(420);
//                    myPinky.setY(100);
//                    inky.setX(420);
//                    inky.setY(580);
//                    myC.setX(100);
//                    myC.setY(580);
//                    try {
//                        Thread.sleep(2000);
//                    } catch (InterruptedException e) {
//                        e.printStackTrace();
//                    }
//                } else {
//                    on_off = false;
//                }
//            }
//            if (myC.gotya(myP.getX(), myP.getY())) {
//                if (myP.getLife() > 1) {
//                    myP.setLife(myP.getLife() - 1);
//                    myP.setX(280);
//                    myP.setY(340);
//                    myB.setY(100);
//                    myB.setX(100);
//                    myPinky.setX(420);
//                    myPinky.setY(100);
//                    inky.setX(420);
//                    inky.setY(580);
//                    myC.setX(100);
//                    myC.setY(580);
//                    try {
//                        Thread.sleep(2000);
//                    } catch (InterruptedException e) {
//                        e.printStackTrace();
//                    }
//                } else {
//                    on_off = false;
//                }
//            }
//            if (inky.gotya(myP.getX(), myP.getY())) {
//                if (myP.getLife() > 1) {
//                    myP.setLife(myP.getLife() - 1);
//                    myP.setX(280);
//                    myP.setY(340);
//                    myB.setY(100);
//                    myB.setX(100);
//                    myB.setDirection(4);
//                    myPinky.setX(420);
//                    myPinky.setY(100);
//                    myPinky.setDirection(2);
//                    inky.setX(420);
//                    inky.setY(580);
//                    myC.setX(100);
//                    myC.setY(580);
//                    try {
//                        Thread.sleep(2000);
//                    } catch (InterruptedException e) {
//                        e.printStackTrace();
//                    }
//                } else {
//                    on_off = false;
//                }
//            }
            if (i % 20 == 0) {
                myPinky.setDirection(myPinky.chase2(myP.getX(), myP.getY(), myP.getDirection()));
                if (myB.getMode() == 1) {
                    int dir = myB.chase(myP.getX(), myP.getY());
                    if(dir != myB.getDirection()){
                        System.out.println("Blinky dir change: " + myB.getX() + " " + myB.getY() + " " + myB.getDirection());
                    }
                    myB.setDirection(dir);
                }
                inky.setDirection(inky.chase(myP.getX(), myP.getY(), myP.getDirection(), myB.getX(), myB.getY()));

                double gyok = sqrt(((myP.getX() / 20) - (myC.getX() / 20)) * ((myP.getX() / 20) - (myC.getX()) / 20) + ((myP.getY() / 20) - (myC.getY()) / 20) * ((myP.getY() / 20) - (myC.getY() / 20)));
                if (gyok > 10) {
                    myC.setDirection(myC.chase(myP.getX(), myP.getY()));
                } else {
                    myC.setDirection(myC.scatter());
                }

            }
        }
        myN.setDead(true);
        try {
            Thread.sleep(4000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        main.showMenu();
    }
}
