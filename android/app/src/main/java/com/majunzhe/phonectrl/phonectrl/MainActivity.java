package com.majunzhe.phonectrl.phonectrl;

import android.app.Activity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;

import module.Command;


public class MainActivity extends Activity {

    private Button btnShutdown;
    private Button btnSuspend;
    private Button btnReboot;
    private Button btnLogout;
    private Command command;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        btnShutdown = (Button)findViewById(R.id.btn_shutdown);
        btnSuspend = (Button)findViewById(R.id.btn_suspend);
        btnReboot = (Button)findViewById(R.id.btn_reboot);
        btnLogout = (Button)findViewById(R.id.btn_logout);
        command = new Command();

        btnShutdown.setOnClickListener(btnListener);
        btnSuspend.setOnClickListener(btnListener);
        btnReboot.setOnClickListener(btnListener);
        btnLogout.setOnClickListener(btnListener);
    }

    private View.OnClickListener btnListener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            Thread th;
            switch (v.getId()){
                case R.id.btn_shutdown:
                    th = new Thread() {
                        @Override
                        public void run() {
                            super.run();
                            command.shutdown();
                        }
                    };
                    th.start();
                    break;
                case R.id.btn_suspend:
                    th = new Thread() {
                        @Override
                        public void run() {
                            super.run();
                            command.suspend();
                        }
                    };
                    th.start();
                    break;
                case R.id.btn_reboot:
                    th = new Thread() {
                        @Override
                        public void run() {
                            super.run();
                            command.reboot();
                        }
                    };
                    th.start();
                    break;
                case R.id.btn_logout:
                    th = new Thread() {
                        @Override
                        public void run() {
                            super.run();
                            command.logout();
                        }
                    };
                    th.start();
                    break;
                default:
                    break;
            }
        }
    };

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            return true;
        }
        return super.onOptionsItemSelected(item);
    }
}
