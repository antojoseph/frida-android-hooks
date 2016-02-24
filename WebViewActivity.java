package com.jni.anto.kalip;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.webkit.WebView;


public class WebViewActivity extends AppCompatActivity {



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        WebView w = (WebView) findViewById(R.id.webView);
        w.loadUrl("http://www.frida.re/");
        w.getSettings().setJavaScriptEnabled(true);

                }
            }






