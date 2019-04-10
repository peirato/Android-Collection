package com.peirato.retrofitdome;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.TextView;

import com.peirato.bean.WertherBean;
import com.peirato.builder.RetrofitBuilder;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        final TextView tv = (TextView) findViewById(R.id.tv);

        RetrofitBuilder.build()
//                .param("city","beijing")   //该请求不需要参数 如果需要参数这么写就行
//                .param("day","2.14")
                .get("/data/sk/101010100.html", new RetrofitBuilder.CallBack<WertherBean>() {
            @Override
            public void onSuccess(WertherBean bean) {

                tv.setText(bean.getWeatherinfo().toString());

            }

            @Override
            public void onError(String errMsg) {

            }

            @Override
            public void onFailure() {

            }
        });
    }
}
