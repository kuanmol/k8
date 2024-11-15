package com.example.user_service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RestController
public class UserController {

    @Autowired
    private RestTemplate restTemplate;

    @GetMapping("/get-order-info")
    public String getOrderInfo() {
        String orderServiceUrl = "http://order-service/orders/info"; // Eureka resolves "order-service"
        return restTemplate.getForObject(orderServiceUrl, String.class);
    }
}
