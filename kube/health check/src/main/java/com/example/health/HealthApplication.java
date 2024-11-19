package com.example.health;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
public class HealthApplication {

    public static void main(String[] args) {
        SpringApplication.run(HealthApplication.class, args);
    }


    @RestController
    class HealthController {

        @GetMapping("/ready")
        public ResponseEntity<String> readinessProbe() {
            return ResponseEntity.ok("Ready");
        }

        @GetMapping("/health")
        public ResponseEntity<String> livenessProbe() {
            return ResponseEntity.ok("Healthy");
        }
    }
}
