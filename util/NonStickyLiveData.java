package com.wl.test;

import androidx.annotation.NonNull;
import androidx.lifecycle.LifecycleOwner;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.Observer;

import java.util.concurrent.ConcurrentHashMap;


public class NonStickyLiveData<T> extends androidx.lifecycle.LiveData<T> {
    private ConcurrentHashMap<androidx.lifecycle.Observer, ObserverWrapper> observerMapping = new ConcurrentHashMap<>();

    @Override
    public void observe(@androidx.annotation.NonNull LifecycleOwner owner, @androidx.annotation.NonNull androidx.lifecycle.Observer<? super T> observer) {
        super.observe(owner, wrap(observer));
    }

    @Override
    public void observeForever(@androidx.annotation.NonNull androidx.lifecycle.Observer<? super T> observer) {
        super.observeForever(wrap(observer));
    }

    @Override
    public void removeObserver(@androidx.annotation.NonNull androidx.lifecycle.Observer<? super T> observer) {
        ObserverWrapper wrapper = observerMapping.remove(observer);
        if (wrapper != null) {
            super.removeObserver(wrapper);
        } else {
            super.removeObserver(observer);
        }
    }

    @Override
    public void postValue(T value) {
        super.postValue(value);
    }

    @Override
    public void setValue(T value) {
        super.setValue(value);
    }

    private androidx.lifecycle.Observer wrap(androidx.lifecycle.Observer<? super T> observer) {
        ObserverWrapper proxyObserver = new ObserverWrapper(observer);
        observerMapping.put(observer, proxyObserver);
        return proxyObserver;
    }

    /**
     * 包装observer。可以忽略第一次的onChanged回调
     * @param <T>
     */
    private class ObserverWrapper<T> implements androidx.lifecycle.Observer<T> {
        private final androidx.lifecycle.Observer targetObserver;
        private boolean ignoreOnce;

        public ObserverWrapper(androidx.lifecycle.Observer targetObserver) {
            this.targetObserver = targetObserver;
            this.ignoreOnce = getValue() != null;
        }

        @Override
        public void onChanged(T t) {
            if (ignoreOnce) {
                ignoreOnce = false;
            } else {
                targetObserver.onChanged(t);
            }
        }
    }
}
