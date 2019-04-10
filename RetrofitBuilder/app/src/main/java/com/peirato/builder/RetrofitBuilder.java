package com.peirato.builder;

import android.util.Log;

import com.google.gson.Gson;
import com.peirato.bean.BaseBean;

import java.io.IOException;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import okhttp3.ResponseBody;
import retrofit2.Retrofit;
import retrofit2.adapter.rxjava.RxJavaCallAdapterFactory;
import retrofit2.http.GET;
import retrofit2.http.POST;
import retrofit2.http.QueryMap;
import retrofit2.http.Url;
import rx.Observable;
import rx.Subscriber;
import rx.android.schedulers.AndroidSchedulers;
import rx.schedulers.Schedulers;


/**
 * Created by peirato on 2017/2/13.
 */

public class RetrofitBuilder {
    private Retrofit retrofit;
    private static RetrofitBuilder retrofitBuilder;
    private Map<String, String> params;
    private static final String TAG = "RetrofitBuilder";


    private RetrofitBuilder() {

        retrofit = new Retrofit.Builder()
                .baseUrl("http://www.weather.com.cn") //填入baseUrl
                .addCallAdapterFactory(RxJavaCallAdapterFactory.create())
                .build();
        params = new HashMap<>();

    }

    public static RetrofitBuilder build() {

        retrofitBuilder = new RetrofitBuilder();
        return retrofitBuilder;

    }


    public <B extends BaseBean> void post(String url, final CallBack<B> callBack) {

        RetrofitService server = retrofit.create(RetrofitService.class);

        final Type[] types = callBack.getClass().getGenericInterfaces();

        final Type finalNeedType = MethodHandler(types).get(0);

        server.post(url, params)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Subscriber<ResponseBody>() {
                    @Override
                    public void onCompleted() {

                    }

                    @Override
                    public void onError(Throwable e) {
                        Log.e(TAG,e.getMessage());
                        callBack.onFailure();
                    }

                    @Override
                    public void onNext(ResponseBody responseBody) {
                        try {
                            B data = new Gson().fromJson(responseBody.string(), finalNeedType);
                            if (data.getRecode() == 0) {
                                callBack.onSuccess(data);
                            } else {
                                callBack.onError(data.getErrmsg());
                            }
                        } catch (IOException e) {
                            Log.e(TAG,e.getMessage());
                            e.printStackTrace();
                        }

                    }


                });

    }

    public <B extends BaseBean> void get(String url, final CallBack<B> callBack) {

        RetrofitService server = retrofit.create(RetrofitService.class);

        final Type[] types = callBack.getClass().getGenericInterfaces();

        final Type finalNeedType = MethodHandler(types).get(0);

        server.get(url, params)
                .subscribeOn(Schedulers.io())
                .observeOn(AndroidSchedulers.mainThread())
                .subscribe(new Subscriber<ResponseBody>() {
                    @Override
                    public void onCompleted() {

                    }

                    @Override
                    public void onError(Throwable e) {
                        Log.e(TAG,e.getMessage());
                        callBack.onFailure();
                    }

                    @Override
                    public void onNext(ResponseBody responseBody) {
                        try {
                            B data = new Gson().fromJson(responseBody.string(), finalNeedType);

//                            if (data.getRecode() == 0) {   //这里根据实际使用情况判断
//                                callBack.onSuccess(data);
//                            } else {
//                                callBack.onError(data.getErrmsg());
//                            }
                            callBack.onSuccess(data);
                        } catch (IOException e) {
                            Log.e(TAG,e.getMessage());
                            e.printStackTrace();
                        }

                    }


                });

    }

    public RetrofitBuilder param(String key, String value) {
        params.put(key, value);
        return retrofitBuilder;
    }


    public interface RetrofitService {

        @POST()
        Observable<ResponseBody> post(@Url String url,
                                      @QueryMap Map<String, String> map);

        @GET()
        Observable<ResponseBody> get(@Url String url,
                                      @QueryMap Map<String, String> map);

    }

    public interface CallBack<B extends BaseBean> {   //回调接口的方法和BaseBean根据实际情况来写

        void onSuccess(B b);

        void onError(String errMsg);

        void onFailure();

    }


    private List<Type> MethodHandler(Type[] types) {
        List<Type> needtypes = new ArrayList<>();

        for (Type paramType : types) {
            if (paramType instanceof ParameterizedType) {
                Type[] parentypes = ((ParameterizedType) paramType).getActualTypeArguments();
                for (Type childtype : parentypes) {
                    needtypes.add(childtype);
                    if (childtype instanceof ParameterizedType) {
                        Type[] childtypes = ((ParameterizedType) childtype).getActualTypeArguments();
                        for (Type type : childtypes) {
                            needtypes.add(type);
                        }
                    }
                }
            }
        }
        return needtypes;
    }


}
