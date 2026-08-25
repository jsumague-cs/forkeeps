import { StatusBar } from "expo-status-bar";
import { Pressable, SafeAreaView, StyleSheet, Text, View } from "react-native";
import { colors } from "../theme/colors";

export function CoupleSetupScreen() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar style="dark" />
      <View style={styles.screen}>
        <View style={styles.brandRow}>
          <Text style={styles.brandMark}>♥</Text>
          <Text style={styles.brandName}>forkeeps</Text>
        </View>

        <View style={styles.connectionCard}>
          <View style={styles.avatarRow}>
            <View style={[styles.avatar, styles.avatarCoral]}>
              <Text style={styles.avatarText}>A</Text>
            </View>

            <View style={styles.connectorWrap}>
              <View style={styles.connectorLine} />
              <View style={styles.connectorBadge}>
                <Text style={styles.connectorHeart}>♥</Text>
              </View>
            </View>

            <View style={[styles.avatar, styles.avatarSage]}>
              <Text style={styles.avatarText}>J</Text>
            </View>
          </View>

          <View style={styles.accountLabels}>
            <View style={styles.labelRow}>
              <View style={[styles.labelDot, styles.coralDot]} />
              <Text style={styles.labelText}>Your account</Text>
            </View>
            <View style={styles.labelRow}>
              <Text style={styles.labelText}>Partner's account</Text>
              <View style={[styles.labelDot, styles.sageDot]} />
            </View>
          </View>

          <View style={styles.sharedBadge}>
            <Text style={styles.sharedIcon}>♥</Text>
            <Text style={styles.sharedText}>One shared couple space</Text>
          </View>
        </View>

        <View style={styles.copyBlock}>
          <Text style={styles.title}>Create your couple space</Text>
          <Text style={styles.subtitle}>
            Start together, keep memories together.
          </Text>
        </View>

        <View style={styles.actions}>
          <Pressable style={styles.primaryButton}>
            <Text style={styles.primaryIcon}>♥</Text>
            <Text style={styles.primaryButtonText}>Invite my partner</Text>
          </Pressable>

          <Pressable style={styles.outlineButton}>
            <Text style={styles.outlineButtonText}>I have an invite code</Text>
          </Pressable>
        </View>

        <View style={styles.privacyRow}>
          <Text style={styles.lockIcon}>♙</Text>
          <Text style={styles.privacyText}>
            Private & encrypted · Only you two can see this
          </Text>
        </View>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.background,
  },
  screen: {
    flex: 1,
    paddingHorizontal: 28,
    paddingTop: 17,
    backgroundColor: colors.background,
  },
  brandRow: {
    height: 48,
    flexDirection: "row",
    alignItems: "flex-start",
    gap: 7,
  },
  brandMark: {
    color: colors.primary,
    fontSize: 12,
    lineHeight: 18,
  },
  brandName: {
    color: colors.text,
    fontSize: 18,
    lineHeight: 27,
    fontWeight: "800",
  },
  connectionCard: {
    height: 234,
    borderRadius: 34,
    borderWidth: 1,
    borderColor: colors.panelBorder,
    paddingHorizontal: 27,
    paddingTop: 29,
    alignItems: "center",
    backgroundColor: "#FEF7F4",
    shadowColor: "#1F2933",
    shadowOpacity: 0.04,
    shadowRadius: 18,
    shadowOffset: { width: 0, height: 8 },
    elevation: 1,
  },
  avatarRow: {
    width: "100%",
    flexDirection: "row",
    alignItems: "center",
  },
  avatar: {
    width: 70,
    height: 70,
    borderRadius: 35,
    alignItems: "center",
    justifyContent: "center",
  },
  avatarCoral: {
    backgroundColor: colors.primary,
    shadowColor: colors.primary,
    shadowOpacity: 0.28,
    shadowRadius: 11,
    shadowOffset: { width: 0, height: 7 },
    elevation: 5,
  },
  avatarSage: {
    backgroundColor: colors.sage,
    shadowColor: colors.sage,
    shadowOpacity: 0.28,
    shadowRadius: 11,
    shadowOffset: { width: 0, height: 7 },
    elevation: 5,
  },
  avatarText: {
    color: colors.card,
    fontSize: 28,
    lineHeight: 42,
    fontWeight: "800",
  },
  connectorWrap: {
    flex: 1,
    height: 36,
    alignItems: "center",
    justifyContent: "center",
    paddingHorizontal: 10,
  },
  connectorLine: {
    width: "100%",
    borderTopWidth: 1.5,
    borderStyle: "dashed",
    borderColor: "rgba(232, 122, 109, 0.22)",
  },
  connectorBadge: {
    position: "absolute",
    width: 35,
    height: 35,
    borderRadius: 18,
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: colors.softCoral,
    shadowColor: colors.primary,
    shadowOpacity: 0.14,
    shadowRadius: 5,
    shadowOffset: { width: 0, height: 2 },
    elevation: 2,
  },
  connectorHeart: {
    color: colors.primary,
    fontSize: 13,
    lineHeight: 18,
  },
  accountLabels: {
    width: "100%",
    marginTop: 24,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
  },
  labelRow: {
    flexDirection: "row",
    alignItems: "center",
    gap: 5,
  },
  labelDot: {
    width: 7,
    height: 7,
    borderRadius: 2,
  },
  coralDot: {
    backgroundColor: colors.primary,
  },
  sageDot: {
    backgroundColor: colors.sage,
  },
  labelText: {
    color: colors.quietText,
    fontSize: 13,
    lineHeight: 19,
    fontWeight: "600",
  },
  sharedBadge: {
    marginTop: 25,
    minHeight: 34,
    paddingHorizontal: 18,
    paddingVertical: 8,
    borderRadius: 25,
    borderWidth: 1,
    borderColor: colors.border,
    backgroundColor: "rgba(255, 255, 255, 0.85)",
    flexDirection: "row",
    alignItems: "center",
    gap: 8,
    shadowColor: colors.text,
    shadowOpacity: 0.05,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 3 },
    elevation: 1,
  },
  sharedIcon: {
    color: colors.primary,
    fontSize: 12,
  },
  sharedText: {
    color: "#6B7280",
    fontSize: 14,
    lineHeight: 20,
    fontWeight: "600",
  },
  copyBlock: {
    marginTop: 38,
  },
  title: {
    color: colors.text,
    fontSize: 31,
    lineHeight: 37,
    fontWeight: "800",
  },
  subtitle: {
    marginTop: 10,
    color: colors.mutedText,
    fontSize: 17,
    lineHeight: 26,
    fontWeight: "500",
  },
  actions: {
    marginTop: 32,
    gap: 15,
  },
  primaryButton: {
    minHeight: 61,
    borderRadius: 25,
    backgroundColor: colors.primary,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 10,
    shadowColor: colors.primary,
    shadowOpacity: 0.3,
    shadowRadius: 15,
    shadowOffset: { width: 0, height: 10 },
    elevation: 4,
  },
  primaryIcon: {
    color: colors.card,
    fontSize: 14,
    lineHeight: 18,
  },
  primaryButtonText: {
    color: colors.card,
    fontSize: 17,
    lineHeight: 25,
    fontWeight: "800",
  },
  outlineButton: {
    minHeight: 58,
    borderRadius: 25,
    borderWidth: 1.5,
    borderColor: colors.border,
    backgroundColor: colors.card,
    alignItems: "center",
    justifyContent: "center",
  },
  outlineButtonText: {
    color: colors.text,
    fontSize: 16,
    lineHeight: 24,
    fontWeight: "700",
  },
  privacyRow: {
    marginTop: 30,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 6,
  },
  lockIcon: {
    color: colors.quietText,
    fontSize: 11,
    lineHeight: 16,
  },
  privacyText: {
    color: colors.quietText,
    fontSize: 12,
    lineHeight: 18,
    fontWeight: "500",
  },
});
