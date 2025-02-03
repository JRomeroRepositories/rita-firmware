
class SensorDriver {
  public:
    SensorDriver(int pin);
    int sensor_read_val();
  private:
    const int SENSOR_PIN;
};