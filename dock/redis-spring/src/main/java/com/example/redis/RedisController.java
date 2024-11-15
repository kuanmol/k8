import org.springframework.beans.factory.annotation.Value;
import org.springframework.data.redis.core.StringRedisTemplate;
import org.springframework.web.bind.annotation.*;

import java.util.concurrent.TimeUnit;
import java.util.logging.Logger;

@RestController
@RequestMapping("/redis")
public class RedisController {

    private final StringRedisTemplate redisTemplate;
    private static final Logger logger = Logger.getLogger(RedisController.class.getName());

    @Value("${spring.redis.password}")
    private String redisPassword;

    public RedisController(StringRedisTemplate redisTemplate) {
        this.redisTemplate = redisTemplate;
    }

    @PostMapping("/set")
    public Response setRedisData(@RequestBody KeyValue keyValue) {
        try {
            logger.info("Setting value in Redis: " + keyValue.getKey() + " = " + keyValue.getValue());
            redisTemplate.opsForValue().set(keyValue.getKey(), keyValue.getValue(), 10, TimeUnit.MINUTES);
            return new Response("Data set successfully: " + keyValue.getKey());
        } catch (Exception e) {
            logger.severe("Error setting data in Redis: " + e.getMessage());
            return new Response("Error setting data in Redis: " + e.getMessage());
        }
    }

    @GetMapping("/get")
    public Response getRedisData(@RequestParam String key) {
        try {
            logger.info("Getting value from Redis: " + key);
            String value = redisTemplate.opsForValue().get(key);
            return new Response(value != null ? value : "No value found");
        } catch (Exception e) {
            logger.severe("Error fetching data from Redis: " + e.getMessage());
            return new Response("Error fetching data from Redis");
        }
    }

    public static class KeyValue {
        private String key;
        private String value;

        // getters and setters
        public String getKey() {
            return key;
        }

        public void setKey(String key) {
            this.key = key;
        }

        public String getValue() {
            return value;
        }

        public void setValue(String value) {
            this.value = value;
        }
    }

    public static class Response {
        private String message;

        public Response(String message) {
            this.message = message;
        }

        public String getMessage() {
            return message;
        }

        public void setMessage(String message) {
            this.message = message;
        }
    }
}
