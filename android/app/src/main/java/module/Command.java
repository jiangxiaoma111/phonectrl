package module;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

/**
 * Created by mjz on 14-11-8.
 * It's used to send command to the computer.
 */
public class Command {

    public void shutdown() {
        DatagramSocket socket;
        byte buff[] = {Constants.SHUTDOWN};
        DatagramPacket dgramPack;
        try {
            socket = new DatagramSocket();
            dgramPack = new DatagramPacket(buff, buff.length,
                    InetAddress.getByName("255.255.255.255"),
                    Constants.PORT);
            socket.send(dgramPack);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public void halt() {
    }

    public void reboot() {
    }
}
